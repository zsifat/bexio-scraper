from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import re
import urllib.error

# URL and headers
url = 'https://motionview.com.bd'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

try:
    # Making the request
    request = Request(url, headers=headers)
    html = urlopen(request)

    # Parsing the HTML
    bs = BeautifulSoup(html, 'html.parser')

    # Finding all paragraphs that contain the word 'Smartwatch'
    products = bs.find_all('div', string=re.compile('.*Smartwatch.*'))

    # Printing the text of each product found
    for product in products:
        prdct = product.get_text()
        print(prdct)

except urllib.error.URLError as e:
    print(f"Failed to open the URL: {e.reason}")
except Exception as e:
    print(f"An error occurred: {str(e)}")

