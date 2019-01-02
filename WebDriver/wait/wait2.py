from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from time import ctime
from time import sleep

driver=webdriver.Firefox()
driver.get("http://www.baidu.com/")
driver.maximize_window()
sleep(2)
#隐式等待5s
driver.implicitly_wait(5)
#检查搜索框是否存在
try:
    print(ctime())
    driver.find_element_by_css_selector("#kw").send_keys("python")
    driver.find_element_by_css_selector("#su").click()
except NoSuchElementException as msg:
    print(msg)
finally:
    print(ctime())