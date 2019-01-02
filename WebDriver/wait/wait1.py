from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from time import sleep

driver=webdriver.Firefox()
driver.get("http://www.baidu.com/")
driver.maximize_window()
sleep(2)
driver.find_element_by_css_selector("#kw").send_keys("python")
#显式等待，判断搜索按钮是否存在,设置最长等待时间为5s,每隔5s检查一次
element=WebDriverWait(driver,5,0.5).until(expected_conditions.presence_of_element_located(By.ID,"su"))

element.click()