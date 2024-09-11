import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


deptfacultylink='https://www.sust.edu/d/pme/faculty'

driver=webdriver.Chrome()
driver.get(deptfacultylink)
driver.implicitly_wait(3)
wait=WebDriverWait(driver,10)
buttons=wait.until(expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR,'a[data-largesrc="images/staff/large/"]')))

teacher_link_list=[]
i=0
for button in buttons:
    i+=1
    try:
        button.click()
        time.sleep(1)

        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        teacherlink = soup.find_all('a', href=re.compile(r'https://www.sust.edu/d/pme/faculty-profile-detail/\d+$'))

        for link in teacherlink:
            teacher_link_list.append(link['href'])
            print(link['href'])
        button.click()
    except Exception:
        print(Exception)
print(len(teacher_link_list))
print(i)
driver.quit()
