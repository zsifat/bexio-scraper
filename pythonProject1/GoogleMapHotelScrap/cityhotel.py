from module1 import get_hotel_info


def get_html(city):

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
    link='https://www.google.com/maps/search/hotel+'
    link+=city
    link+='?hl=en'
    driver.get(link)
    time.sleep(4)

    try:
        # Wait for the container to load
        wait = WebDriverWait(driver, 10)
        container = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]')))
        logging.info("Container found. Starting scrolling process.")

        end_reached = False
        last_height = driver.execute_script("return arguments[0].scrollHeight;", container)

        while not end_reached:
            # Scroll within the container
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", container)
            logging.info("Scrolling...")
            time.sleep(3)  # Adjust the sleep time as necessary

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


def get_hotel_infos(city):
    from bs4 import BeautifulSoup
    hotel_infos = []

    # Get HTML content
    html = get_html(city)

    # Parse HTML
    bs = BeautifulSoup(html, 'html.parser')

    # Get list of <a> tags
    a_list = bs.find_all('a',class_='hfpxzc')

    # Print out the hrefs
    for a in a_list:
        href = a.get('href')

    # Extract hotel info from each link
    for a in a_list:
        link = a.get('href')
        if not link.startswith('http'):
            link = 'https://www.google.com' + link  # Ensure it is a complete URL
        hotelinfo = get_hotel_info(link)
        hotel_infos.append(hotelinfo)

    return hotel_infos


def get_hotel_csv(city,filename):
    import csv
    hotel_infos=get_hotel_infos(city)
    with open(filename,'w',newline='',encoding='utf-8') as file:
        writer=csv.writer(file)
        writer.writerow(['Title','Address','Phone No'])
        for infos in hotel_infos:
            writer.writerow(infos)


city='narsingdi'
filename='narsingdi_hotel_infos.csv'
get_hotel_csv(city,filename)



