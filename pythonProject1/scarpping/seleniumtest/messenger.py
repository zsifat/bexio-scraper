import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def send_message(driver, chat_url, message, num_messages=19):
    # Navigate to the chat
    driver.get(chat_url)

    # Create a WebDriverWait object
    wait = WebDriverWait(driver, 20)

    try:
        for i in range(num_messages):
            # Wait for the text box to be visible
            text = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[role="textbox"]')))
            text.send_keys(message)

            # Wait for the send button to be clickable
            send_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Press enter to send"]')))

            # Scroll to the button to ensure it is in view
            driver.execute_script("arguments[0].scrollIntoView(true);", send_button)

            # Optionally wait until overlapping elements are no longer visible
            try:
                WebDriverWait(driver, 10).until(
                    EC.invisibility_of_element_located((By.CSS_SELECTOR, '__fb-dark-mode'))
                )
            except:
                print("Overlapping elements may be present but are not disappearing.")

            # Click the send button using JavaScript if needed
            driver.execute_script("arguments[0].click();", send_button)
            print(f"Message {i+1} sent successfully!")

            # Optionally add a short delay between messages
            time.sleep(2)

    except Exception as e:
        print(f"An error occurred: {e}")

# Set up the driver
driver = webdriver.Chrome()
driver.get('https://www.messenger.com')

# Wait for manual login
print("Please log in to Messenger manually. The script will continue after 30 seconds.")
time.sleep(40)

# Send messages to the first chat
send_message(driver, 'https://www.messenger.com/t/6888184394564484', 'Automated: This message will be sent 5 times.',5)

# Send messages to the second chat


# Allow some time to see the result before closing the browser
print("The browser will remain open for 10 seconds. Press Enter to close it early.")
input()
driver.quit()
