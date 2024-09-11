import re
import csv
from os import write

from module1 import get_hotel_info


def get_html(keyword):

    import logging
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import time

    # Configure logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Start the WebDriver
    driver = webdriver.Chrome()
    link='https://www.google.com/maps/search/'
    link+=keyword
    link+='?hl=en'
    driver.get(link)
    time.sleep(3)

    try:
        # Wait for the container to load
        wait = WebDriverWait(driver, 10)

        container = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]')))
        logging.info("Container found. Starting scrolling process.")

        end_reached = False
        last_height = driver.execute_script("return arguments[0].scrollHeight;", container)

        while not end_reached:
            # Scroll within the container
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", container)
            logging.info("Scrolling...")
            time.sleep(4)  # Adjust the sleep time as necessary

            # Calculate the new height after scrolling
            new_height = driver.execute_script("return arguments[0].scrollHeight;", container)

            if new_height == last_height:
                # No more new content loaded
                logging.info("Reached the end of the scrollable content.")
                end_reached = True
            else:
                last_height = new_height

    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        # Ensure the driver quits
        html=driver.page_source
        logging.info("Closing the driver.")
        driver.quit()
        logging.info("Driver closed.")
        return html


def get_company_infos(keyword):
    from bs4 import BeautifulSoup


    # Get HTML content
    html = get_html(keyword)

    # Parse HTML
    bs = BeautifulSoup(html, 'html.parser')
    containers=bs.select('div.Nv2PK.tH5CWc.THOPZb')

    company_infos=[]

    for container in containers:
        company_info=[]
        company_name_list = container.select('div.qBF1Pd.fontHeadlineSmall')
        for company_name_tag in company_name_list:
            company_name=company_name_tag.get_text()
        company_info.insert(0,company_name)
        print(company_name)

        company_type_tags_list = container.select('div.UaQhfb.fontBodyMedium span > span')
        for company_type_tags in company_type_tags_list:
            if 'cleaning' in company_type_tags.get_text().lower():
                company_type = company_type_tags.get_text().title()
        company_info.insert(1, company_type)
        print(company_type)

        company_address_tags_list = container.select('div.UaQhfb.fontBodyMedium span > span')
        for company_address_tags in company_address_tags_list:
            if 'cleaning' not in company_address_tags.get_text().lower():
                company_address = company_type_tags.get_text()
        #company_info.insert(1, company_type)
        print(company_address)


        company_contact_tag=container.select_one('.UsdlK')
        if company_contact_tag:
            company_phoneNo=company_contact_tag.get_text(strip=True)
        else:
            company_phoneNo='-'
        company_info.insert(2, company_phoneNo)
        print(company_phoneNo)
        company_infos.append(company_info)
        print('-----------')

    return company_infos


filename='cleaning_service_sydney.csv'

with open(filename,'w',newline='',encoding='utf-8') as file:
    writer=csv.writer(file)
    writer.writerow(['Company Name','Company Type','Contact No'])
    company_infos=get_company_infos('cleaning+service+sydney')
    for infos in company_infos:
        writer.writerow(infos)

print('-----------Completed----------')







