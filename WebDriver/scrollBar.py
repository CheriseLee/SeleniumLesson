from selenium import webdriver
from time import sleep
from time import ctime
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Firefox()
driver.get("http://www.51zxw.net")
driver.maximize_window()

js="var action=document.documentElement.scrollTop=10000"
driver.execute_script(js)
sleep(2)
js="var action=document.documentElement.scrollTop=0"
driver.execute_script(js)
driver.get_screenshot_as_file(r'D:\Selenium\WebDriver\51zxw.png')