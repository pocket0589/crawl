import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crawling.settings")

django.setup()

from naver.views import get_single_article
from naver.models import Article, Publisher

def main(url=None):
    if url is None:
        url = 'http://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=101&oid=052&aid=0000791309'
    data = get_single_article(url)
    publisher, pub_created = Publisher.objects.get_or_create(name=data['publisher'])
    article, article_created = Article.objects.get_or_create(
                                   title=data['title'],
                                   body='\n'.join([content.prettify() for content in data['content_list']]),
                                   url=data['url']
                               )
    if pub_created:
        print('Publisher "' + data['publisher'] + '" has created.')
    if article_created:
        print('Article "' + data['title'] + '" has created.')

if __name__ == '__main__':

    main()
