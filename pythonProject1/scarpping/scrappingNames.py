from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen('https://www.pythonscraping.com/pages/warandpeace.html')
bs=BeautifulSoup(html.read(),'html.parser')

namelist=bs.find_all('span',{'class':'green'})
namelist=set(namelist)

for name in namelist:
    print(name.get_text().title())

