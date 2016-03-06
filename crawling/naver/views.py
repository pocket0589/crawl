from django.shortcuts import render

import requests
from bs4 import BeautifulSoup
import re

def remove_html_tags(data):
    p = re.compile(r'<.*?>')
    return p.sub('\n',data)

def get_single_article(item_url):
    source_code = requests.get(item_url)
    plain_text=source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    title = soup.select('#articleTitle')[0].get_text()
    url=item_url
    publisher=soup.select('.press_logo > a > img')[0].attrs['title']

    #title, url, author, publisher, date
    for content in soup.select('#articleBodyContents'):
        try:
            content_list.append(content)
        except NameError:
            content_list = [content]

    article_data = {
        'title': title,
        'url': url,
        'publisher': publisher,
        'content_list': content_list,
    }

    return article_data

get_single_article('http://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=101&oid=052&aid=0000791309')
