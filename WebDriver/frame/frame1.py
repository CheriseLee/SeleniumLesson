from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from time import ctime
from time import sleep

driver=webdriver.Firefox()
file_path="file:///D:/Selenium/WebDriver/frame/Frame.html"
#路径转义的另一种写法
# file_path="D:\\Selenium\\WebDriver\\frame\\Frame.html"
driver.get(file_path)
driver.switch_to.frame("search")
#定位到搜索框按钮输入关键词
driver.find_element_by_css_selector('.sec-input').send_keys("python")
driver.maximize_window()
driver.find_element_by_id("stb").click()
sleep(2)

#隐式等待5s