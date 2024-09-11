import re
import requests
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Initialize the webdriver (replace with your own path to the webdriver)


driver = webdriver.Chrome()

# Open the website
driver.get("https://www.bexio.com/en-CH/fiduciary-directory")  # Replace with your target URL
time.sleep(7)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
try:
    # Locate the element
    show_all_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "a[data-track-element='bexio.accountant_directory_overview_list.show_all_accountants']"))
    )

    # Use JavaScript to click the element (even if it's covered by another element)
    driver.execute_script("arguments[0].click();", show_all_button)

    print("Clicked the 'Show All Accountants' link")
    time.sleep(4)
except Exception as e:
    print(f"Error clicking the link: {e}")

finally:
    html=driver.page_source
    driver.quit()

bs=BeautifulSoup(html,'lxml')
links=bs.find_all('a',href=re.compile(r'https://www.bexio.com/en-CH/fiduciary-directory\/\d{1,}$'))
urls=[]
for link in links:
    url=link['href']
    urls.append(url)
print(len(urls))

company_infos=[]

for url in urls :
    company_info=[]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    # Make a GET request with the custom User-Agent
    response = requests.get(url, headers=headers)
    bs=BeautifulSoup(response.text,'lxml')
    name_tag=bs.find('h1',class_='mb-1 text-left font-decima')
    name=name_tag.get_text(strip=True)

    address=name_tag.find_next_sibling('span',class_='text-xl').get_text()



    a_tag=bs.find('a',href=re.compile(r'^tel:.*'))
    contact_tag=a_tag.find('span')
    contact_no=contact_tag.get_text(strip=True)


    link_tag=bs.find('a',target='_blank', class_='text-link')
    if link_tag:
        link=link_tag['href']

    company_info.insert(0,name)
    company_info.insert(1,address)
    company_info.insert(2,contact_no)
    company_info.insert(2,link)
    company_infos.append(company_info)

print(company_infos)

filename='bexio_company_info.csv'
with open(filename,'w',newline='',encoding='utf-8') as file:
    writer=csv.writer(file)
    writer.writerow(['Name','Address','Contact','Website'])
    for infos in company_infos:
        writer.writerow(infos)





