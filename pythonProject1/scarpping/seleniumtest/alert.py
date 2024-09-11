from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get('https://www.selenium.dev/documentation/webdriver/interactions/alerts/')

# Wait until the alert link is present and clickable
wait = WebDriverWait(driver, 20)
alert_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'See a sample prompt')))

# Scroll to the alert link
driver.execute_script("arguments[0].scrollIntoView(true);", alert_link)

# Ensure no other elements are blocking the link
time.sleep(1)  # Small delay to ensure visibility

# Retry clicking the alert link if necessary
for _ in range(3):
    try:
        driver.execute_script('arguments[0].click();',alert_link)
        break
    except Exception as e:
        print(f"Click attempt failed: {e}")
        time.sleep(1)  # Wait before retrying

# Wait for the prompt to appear and switch to it
wait.until(EC.alert_is_present())
alert = driver.switch_to.alert

# Interact with the prompt
alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
alert.send_keys('Hi')
time.sleep(10)
alert.accept()  # Accept the prompt

# Pause for user to observe the result
input("Press Enter to quit...")

# Quit the WebDriver
driver.quit()
