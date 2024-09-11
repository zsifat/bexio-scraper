import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
from certifi import contents
from lxml.builder import unicode

html=urlopen('https://en.wikipedia.org/wiki/Bangladesh')
#bs=BeautifulSoup(html,'lxml')
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>','html.parser')
tag=soup.b
tag.name='blockquote'
tag['class']='verybold'
tag['id']=1
tag.append(' hi')

print(tag.contents)
