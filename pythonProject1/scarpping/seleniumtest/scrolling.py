from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

driver = webdriver.Chrome()
driver.get('https://www.google.com/maps/search/hotel+sylhet')

try:
    # Increase the wait time for elements to load
    wait = WebDriverWait(driver, 10)
    container = wait.until(expected_conditions.presence_of_element_located(
        (By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]')))

    end_reached = False

    while not end_reached:
        # Scroll down within the container
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", container)
        time.sleep(1)

        try:
            # Try to detect the 'end' text or element indicating the end of the scroll
            end_text = wait.until(expected_conditions.presence_of_element_located(
                (By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[245]/div/p/span/span')))
            if end_text:
                end_reached = True

        except:
            # Continue scrolling if the 'end' element is not found
            pass

finally:
    # Ensure driver quits even if there's an error
    driver.quit()
