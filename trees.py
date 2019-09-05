from slenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
driver = webdriver.Chromium()
driver.get('https://www.ecosia.org')
i=1
while True:
    search_bar = driver.find_element_by_type('search')
    search_bar.send_keys('I would like to comission a tree planted')
    search_bar.send_keys(Key.RETURN)
    sleep(1)
    print(i)
    i+=1
