from urllib.request import urlopen
from bs4 import BeautifulSoup
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = 'https://www.google.com/maps/place/Hotel+Victoria+Inn/data=!4m11!3m10!1s0x3755b9f56867eb2f:0xd1058b7f5cc746d4!5m3!1s2024-09-10!4m1!1i2!8m2!3d23.7233869!4d90.400147!16s%2Fg%2F11rg8gmq0q!19sChIJL-tnaPW5VTcR1EbHXH-LBdE?authuser=0&hl=en&rclk=1'

driver = webdriver.Chrome()
driver.get(link)

# Allow time for the page to load
time.sleep(5)

# Wait for the container element to be present
wait = WebDriverWait(driver, 10)
container = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]')))

# Check if the container is scrollable
if container.get_attribute('scrollHeight') > container.get_attribute('clientHeight'):
    print("Container is scrollable.")
else:
    print("Container is not scrollable or has insufficient content.")

# Scroll the container to the top (or a specific position)
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", container)

# Give time for the content to load after scrolling
time.sleep(3)

# Optionally scroll to a specific element within the container
##driver.execute_script("arguments[0].scrollIntoView(true);", target_element)

# Allow time for any potential layout adjustments
time.sleep(3)

html = driver.page_source
# Further processing with BeautifulSoup

driver.quit()

bs = BeautifulSoup(html, 'html.parser')
hotel_info = []

name_elements = bs.select(
    '#QA0Szd > div > div > div.w6VYqd > div:nth-child(2) > div > div.e07Vkf.kA9KIf > div > div > div.TIHn2 > div > div.lMbq3e > div:nth-child(1) > h1')
names = [name_element.string for name_element in name_elements]
print(name_elements)
location_elements = bs.select(
    '#QA0Szd > div > div > div.w6VYqd > div:nth-child(2) > div > div.e07Vkf.kA9KIf > div > div > div.TIHn2 > div > div.lMbq3e > div.LBgpqf > div > div > div.F7nice > span:nth-child(1) > span:nth-child(1)')
locatons = [adress.string for adress in location_elements]
print(location_elements)
phone_elements = bs.select(
    '#QA0Szd > div > div > div.w6VYqd > div:nth-child(2) > div > div.e07Vkf.kA9KIf > div > div > div.TIHn2 > div > div.lMbq3e > div.LBgpqf > div > div > div.F7nice > span:nth-child(2) > span > span')
phone = [phoneno.string for phoneno in phone_elements]
print(phone_elements)
hotel_info.insert(0, names[0])
#hotel_info.insert(1, locatons[0])
#hotel_info.insert(2, phone[0])
print(hotel_info)

driver.quit()