import requests
from bs4 import BeautifulSoup
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
# Make a GET request with the custom User-Agent
url='https://www.bexio.com/en-CH/fiduciary-directory/8578'
response = requests.get(url, headers=headers)
bs = BeautifulSoup(response.text, 'lxml')
name_tag = bs.find('h1', class_='mb-1 text-left font-decima')
name = name_tag.get_text()
print(name)
