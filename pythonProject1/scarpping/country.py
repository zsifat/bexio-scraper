from urllib.request import urlopen,Request
from bs4 import BeautifulSoup


url = 'https://www.scrapethissite.com/pages/simple/'
# Add a user-agent header to the request
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

# Open the URL with the request that includes headers
html = urlopen(req)
bs=BeautifulSoup(html,'lxml')

countries=bs.find_all('h3',class_='country-name')
country_infos=[]
country_names=[]
for country in countries:
    country_info=[]
    country_name=country.get_text(strip=True)
    capital_name=country.find_next('span',class_='country-capital').get_text(strip=True)
    population=country.find_next('span',class_='country-population').get_text(strip=True)
    area=country.find_next('span',class_='country-area').get_text(strip=True)
    country_info.insert(0,country_name)
    country_info.insert(1,capital_name)
    country_info.insert(2,population)
    country_info.insert(3,area)
    country_infos.append(country_info)

print(country_infos)