import time

from selenium import webdriver
from selenium.webdriver import Proxy
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import ProxyType


def test():
    driver=setup()
    title=driver.title
    assert title == "Web form"

    driver.implicitly_wait(0.5)

    tex_box=driver.find_element(by=By.NAME,value='my-text')
    submit_button=driver.find_element(by=By.CSS_SELECTOR,value='button')
    tex_box.send_keys('ALLAH is One')
    submit_button.click()
    message=driver.find_element(by=By.ID,value='message')
    message=message.text
    assert message=='Received!'

    teardown(driver)


def setup():
    options=webdriver.ChromeOptions()
    options.browser_version='stable'
    options.page_load_strategy='eager'
    options.platform_name='any'
    options.accept_insecure_certs=True
    options.timeouts={'script':5000}
    options.unhandled_prompt_behavior='dismiss and notify'
    options.proxy=Proxy({'proxyType':ProxyType.MANUAL,'httpProxy':'http.proxy:1234'})
    driver=webdriver.Chrome(options=options)
    driver.get('https://www.selenium.dev/selenium/web/web-form.html')
    return driver

def teardown(driver):
    driver.quit()

test()