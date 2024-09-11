from urllib.request import urlopen
import urllib.error
from bs4 import BeautifulSoup
import re

pages=set()
def getLinks(pageUrl):
    global pages
    try:
        html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
        bs = BeautifulSoup(html, 'lxml')
        try:
            print(bs.h1.get_text())
            print(bs.find(id='mw-content-text').find_all('p')[1].get_text())
            print(bs.find(id='ca-edit').find('a').attrs['href'])
        except AttributeError:
            print('This page is missing something! Continuing.')
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} for URL: {pageUrl}")
        return
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason} for URL: {pageUrl}")
        return
    links=bs.find_all('a',href=re.compile('^(/wiki/)'))
    for link in links:
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage=link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks('/wiki/Football')