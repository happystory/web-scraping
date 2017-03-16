# coding: utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()


def getLinks(pageUrl):
    html = urlopen('http://en.wikipedia.org' + pageUrl)
    bsObj = BeautifulSoup(html, 'html.parser')
    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(id='mw-content-text').find_all('p')[0])
    except AttributeError:
        print('页面缺少一些属性')

    for link in bsObj.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print('---------------------\n' + newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks('')
