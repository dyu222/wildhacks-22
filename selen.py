# import selenium
# driver = selenium.webdriver.Chrome()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

import time

browser = webdriver.Chrome()
url = 'https://northwestern.bluera.com/northwestern/rpvf-eng.aspx?lang=eng&redi=1&SelectedIDforPrint=0677c83a856bb1494393c73cb959564ba17eb502335e7222a38b25de0c6859eef5f26465225e10261ec097a7b37dab6b&ReportType=2&regl=en-US'
browser.get(url)
time.sleep(5)

username = browser.find_element_by_id("idToken1")
password = browser.find_element_by_id("idToken2")

#change these to real user and password
#prob gona want to add this to a git ignore or something if we actually push
username.send_keys("username")
password.send_keys("password")
# 
# browser.find_element_by_name("callback_2").click()
time.sleep(5)
browser.close()

# username = driver.find_element_by_id('idToken1')
# password = driver.find_element_by_id('idToken2')
# # driver.find_element_by_id('loginForm')
# # username = driver.find_element("idToken1")
# # password = driver.find_element("idToken2")
# username.send_keys("username")
# password.send_keys("password")
# driver.find_element_by_id("loginButton_0").click()
