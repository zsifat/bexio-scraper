import re


def get_hotel_html(link):
    import time
    import logging
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By



    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    driver=webdriver.Chrome()
    driver.get(link)
    time.sleep(3)
    wait=WebDriverWait(driver,7)

    #locate the container to scroll
    container=wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]')))
    logging.info('Container found. Starting scrolling.')

    loop_flag=False
    last_height=driver.execute_script('return arguments[0].scrollHeight;',container)

    while not loop_flag:
        driver.execute_script('arguments[0].scrollTop=arguments[0].scrollHeight;',container)
        logging.info('Scrolling')
        time.sleep(2)

        #calculate new Height
        new_height=driver.execute_script('return arguments[0].scrollHeight;',container)
        if new_height==last_height:
            logging.info('Reached the End')
            loop_flag=True
        else:
            last_height=new_height

    return driver.page_source
    driver.quit()
    logging.info("Driver closed.")


def get_hotel_info(link):
    from bs4 import BeautifulSoup

    html=get_hotel_html(link)
    bs=BeautifulSoup(html,'lxml')
    hotel_info=[]
    #hotel name extract
    hotel_name_tag_list=bs.select('#QA0Szd > div > div > div.w6VYqd > div:nth-child(2) > div > div.e07Vkf.kA9KIf > div > div > div.TIHn2 > div > div.lMbq3e > div:nth-child(1) > h1')
    for hotel_name_tag in hotel_name_tag_list:
        hotel_name=hotel_name_tag.get_text()
        hotel_info.insert(0,hotel_name)

    #hotel adress extract
    hotel_address_tag_list=bs.select('#QA0Szd > div > div > div.w6VYqd > div:nth-child(2) > div > div.e07Vkf.kA9KIf > div > div > div:nth-child(11) > div:nth-child(3) > button > div > div.rogA2c > div.Io6YTe.fontBodyMedium.kR99db.fdkmkc')
    for hotel_address_tag in hotel_address_tag_list:
        hotel_address=hotel_address_tag.get_text()
        hotel_info.insert(1,hotel_address)


    #hotel phone extract
    hotel_contact_tag_list=bs.find_all('div',string=re.compile(r'^(\d{11})|^\d{5}[-\s]?\d{6}'))
    #hotel_contact_tag_list=bs.select('#QA0Szd > div > div > div.w6VYqd > div:nth-child(2) > div > div.e07Vkf.kA9KIf > div > div > div:nth-child(11) > div:nth-child(4) > button > div > div.rogA2c > div.Io6YTe.fontBodyMedium.kR99db.fdkmkc')
    for hotel_contact_tag in hotel_contact_tag_list:
        hotel_contact=hotel_contact_tag.get_text()
        hotel_info.insert(2,hotel_contact)


    return hotel_info



