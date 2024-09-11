import re
from datetime import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup
import random

random.seed(datetime.now().timestamp())
def getLinks(articleURl):
    html=urlopen('https://en.wikipedia.org{}'.format(articleURl))
    bs=BeautifulSoup(html,'html.parser')
    links=bs.find('div',{'id':'bodyContent'}).find_all('a',href=re.compile('^(/wiki/)((?!:).)*$'))
    return links

links=getLinks('/wiki/Kevin_Bacon')

while len(links)>0:
    newArticle=links[random.randint(0,len(links)-1)].attrs['href']
    print(newArticle)
    links=getLinks(newArticle)
    if newArticle=='/wiki/Peso':
        break
