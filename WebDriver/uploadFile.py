from selenium import webdriver
from time import sleep
from time import ctime
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.maximize_window()
sleep(2)
driver.find_element_by_css_selector('.soutu-btn').click()
driver.implicitly_wait(2)
driver.find_element_by_css_selector('.upload-pic').send_keys(r'D:\Selenium\WebDriver\timg.jpg')
