import re
from  urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen('https://pythonscraping.com/pages/page3.html')

bs=BeautifulSoup(html,'lxml')


images=bs.find_all(lambda img:img.has_attr('src') and re.compile(r'\.\.\/img\/gifts/img.*\.jpg').search(img['src']))
for image in images:
    print(image['src'])

