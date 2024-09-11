from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import ElementNotInteractableException, StaleElementReferenceException
import time

# Set up the driver
driver = webdriver.Chrome()

# Navigate to the page
driver.get('https://epayment.sust.edu/fee/library-fine')

# Create a WebDriverWait object
wait = WebDriverWait(driver, 10)


def select_by_index(element_id, index):
    try:
        element = wait.until(EC.presence_of_element_located((By.ID, element_id)))
        select = Select(element)
        select.select_by_index(index)
    except StaleElementReferenceException:
        element = wait.until(EC.presence_of_element_located((By.ID, element_id)))
        select = Select(element)
        select.select_by_index(index)
    except NoSuchElementException:
        print(f"Element with ID '{element_id}' not found.")

# Input the registration number
reg_text = wait.until(EC.presence_of_element_located((By.ID, 'reg')))
reg_text.send_keys('2019336063')

# Select session number
select_by_index('session', 1)

# Select semester
select_by_index('semester', 7)


# Input the mobile number
mobile = wait.until(EC.presence_of_element_located((By.ID, 'mobile')))
mobile.send_keys('01711111111')

# Input the email address
email = wait.until(EC.presence_of_element_located((By.ID, 'email')))
email.send_keys('zahidulislamsifat1@gmail.com')

# Input the amount
amount = wait.until(EC.presence_of_element_located((By.ID, 'amount')))
amount.send_keys('10')

# Click the submit button
submit = wait.until(EC.element_to_be_clickable((By.ID, 'nextButton')))
submit.click()

# Wait for manual closure
print("The browser will remain open. Press Enter to close the script once you've manually closed the browser.")
input("Press Enter to exit...")

# Close the browser
driver.quit()
