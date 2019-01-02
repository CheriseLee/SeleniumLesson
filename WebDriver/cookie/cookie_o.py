from selenium import webdriver
from time import sleep
from time import ctime
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Firefox()
driver.get("http://www.51zxw.net")
driver.maximize_window()
sleep(2)
cookie=driver.get_cookies()
print(cookie)
print(cookie[0])
driver.add_cookie({'name':'tom','value':'18'})
