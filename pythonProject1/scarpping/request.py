import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

def nameprice(link,dict):
    # Construct the URL
    url = f'https://books.toscrape.com{link}'
    print(f"Fetching URL: {url}")  # Debug print to trace the URL
    try:
        html = urlopen(url)
    except Exception as e:
        print(f"Failed to open URL: {url}. Error: {e}")
        return

    bs = BeautifulSoup(html, 'html.parser')

    # Extract categories
    links = bs.find_all('a', href=re.compile(r'catalogue/category/books/'))
    categories = [link.get_text().strip() for link in links]

    # Extract book names and prices

    h3list = bs.find_all('h3')
    for h3 in h3list:
        book_name = h3.a['title']
        book_price = h3.parent.find('p', class_='price_color').get_text()
        dict[book_name] = book_price


    # Handle pagination
    nextpagelink = bs.find('li', class_='next')
    if nextpagelink:
        href = nextpagelink.a['href']
        # Ensure the next page link starts with '/catalogue/'
        next_page_link = href if href.startswith('/catalogue/') else '/catalogue/' + href
        nameprice(next_page_link,dict)
    else:
        print("No more pages to scrape.")

# Initial call
dictionary={}
nameprice('/catalogue/page-1.html',dictionary)

for key,value in dictionary.items():
    value=''.join(re.findall(r'\d',value))
    dictionary[key]=value
dictionary=dict(sorted(dictionary.items(),key=lambda item:item[1],reverse=True))
i=0
for key,value in dictionary.items():
    if i<3:
        print(f'{i+1}-{key}:{value}')
        i+=1
    else:
        break


