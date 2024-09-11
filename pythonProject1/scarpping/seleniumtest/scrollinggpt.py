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
driver.get('https://www.google.com/maps/search/hotel+sylhet')

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
        time.sleep(2)  # Adjust the sleep time as necessary

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
    logging.info("Closing the driver.")
    driver.quit()
    logging.info("Driver closed.")
