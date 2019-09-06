from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
driver = webdriver.Chrome('./chromedriver.exe')
while True:
    driver.get('https://www.ecosia.org')
    search_bar = driver.find_element_by_name('q')
    search_bar.send_keys('I would like to comission a tree planted')
    button = driver.find_element_by_xpath('//*[@id="__layout"]/div/section/div[1]/form/div[2]/button[2]')
    button.click()
    sleep(24)
