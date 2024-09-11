import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen('https://www.tutorialspoint.com/index.htm')
bs=BeautifulSoup(html,'lxml')
links=bs.find_all('a',href=re.compile(r'.*\/index.htm'))
link_list=[]
for link in links:
    link_list.append(link['href'])
print(link_list)

