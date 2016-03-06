from datetime import datetime, tzinfo
import re
import requests
from bs4 import BeautifulSoup

from django.views.generic import ListView, DetailView
from .models import Article, Publisher, Author


class ArticleList(ListView):

    model = Article
    context_object_name = "articles"
    template_name = "naver/article_list.html"

    def get(self, *args, **kwargs):
        source_code = requests.get('http://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=101')
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        for link in soup.select('.sphoto1 > dt > a'):
            data = get_single_article(link.attrs['href'])
            publisher, publisher_created = Publisher.objects.get_or_create(name=data['publisher'])
            # Author needs to be implemented
            article, article_created = Article.objects.update_or_create(title=data['title'], time=data['time'],
                                    defaults={'url': data['url'], 'publisher': publisher, 'body': data['body']})
        return super().get(*args, **kwargs)


class ArticleDetail(DetailView):

    model = Article
    context_object_name = "article"
    template_name = "naver/article_detail.html"


def remove_html_tags(data):
    p = re.compile(r'<.*?>')
    return p.sub('\n',data)

def get_single_article(item_url):
    article = {}
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    article['title'] = soup.select('#articleTitle')[0].string
    article['url'] = item_url
    article['publisher'] = soup.select('.press_logo > a > img')[0].attrs['title']
    article['body'] = soup.select('#articleBodyContents')[0].prettify()
    dt = soup.select('.t11')[0].string + ' +0900'
    article['time'] = datetime.strptime(dt, '%Y-%m-%d %H:%M %z')
    return article
