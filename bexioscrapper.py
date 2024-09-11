import re
import requests
import time
import csv
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Configuration
URL = "https://www.bexio.com/en-CH/fiduciary-directory"
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
OUTPUT_FILE = 'bexio_companies_info.csv'

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def initialize_driver():
    """Initialize and return the Selenium WebDriver."""
    driver = webdriver.Chrome()  # Adjust path if necessary
    return driver


def fetch_page_source(driver, url):
    """Fetch the page source after scrolling and clicking."""
    driver.get(url)
    time.sleep(7)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    try:
        show_all_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR,
                 "a[data-track-element='bexio.accountant_directory_overview_list.show_all_accountants']"))
        )
        driver.execute_script("arguments[0].click();", show_all_button)
        logging.info("Clicked the 'Show All Accountants' link")
        time.sleep(4)
    except Exception as e:
        logging.error(f"Error clicking the link: {e}")

    return driver.page_source


def extract_links(html):
    """Extract and return relevant links from the page source."""
    bs = BeautifulSoup(html, 'lxml')
    links = bs.find_all('a', href=re.compile(r'https://www.bexio.com/en-CH/fiduciary-directory/\d{1,}$'))
    urls = [link['href'] for link in links]
    logging.info(f"Found {len(urls)} links")
    return urls


def scrape_company_info(urls):
    """Scrape company information from the provided URLs."""
    company_infos = []
    headers = {'User-Agent': USER_AGENT}

    for url in urls:
        try:
            response = requests.get(url, headers=headers)
            bs = BeautifulSoup(response.text, 'lxml')

            name_tag = bs.find('h1', class_='mb-1 text-left font-decima')
            name = name_tag.get_text(strip=True)
            address = name_tag.find_next_sibling('span', class_='text-xl').get_text(strip=True)

            a_tag = bs.find('a', href=re.compile(r'^tel:.*'))
            contact_no = a_tag.find('span').get_text(strip=True) if a_tag else 'N/A'

            link_tag = bs.find('a', target='_blank', class_='text-link')
            link = link_tag['href'] if link_tag else 'N/A'

            company_infos.append([name, address, contact_no, link])
            logging.info(f"Scraped info for {name}")
            print('---- ')
        except Exception as e:
            logging.error(f"Error scraping {url}: {e}")

    return company_infos


def save_to_csv(data, filename):
    """Save the extracted data to a CSV file."""
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Address', 'Contact', 'Website'])
        writer.writerows(data)
    logging.info(f"Data saved to {filename}")


def main():
    """Main function to orchestrate the scraping process."""
    driver = initialize_driver()
    try:
        html = fetch_page_source(driver, URL)
        urls = extract_links(html)
        company_infos = scrape_company_info(urls)
        save_to_csv(company_infos, OUTPUT_FILE)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
