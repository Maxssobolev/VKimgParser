import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import os
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time

# меняем урл на нужный
url = "https://vk.com/im?act=browse_images&id=804549"

count = -1
browser = webdriver.Firefox()
browser.get(url)

# Здесь логин от ВК
browser.find_element_by_xpath('//*[@id="email"]').send_keys("+7999999999")
# Здесь пароль
browser.find_element_by_xpath(
    '//*[@id="pass"]').send_keys("cj,jktdvfrcbvcthuttdbx4016")
browser.find_element_by_xpath('//*[@id="login_button"]').click()


time.sleep(3)
browser.get(url)
time.sleep(2)
soup = BeautifulSoup(browser.page_source, 'html.parser')

for i in soup.find_all('img'):
    count += 1
    src = i.get('src')
    try:
        jpg = urlopen(src).read()
        out = open("img/fileNum-{}.jpg".format(count), 'wb')
        out.write(jpg)
        out.close()
    except:
        count += 0
