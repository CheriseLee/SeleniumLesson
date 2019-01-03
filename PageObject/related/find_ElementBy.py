from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()

driver.get("http://www.baidu.com")
driver.implicitly_wait(3)
#通过ID传值
driver.find_element(By.ID,'kw').clear()
driver.find_element(By.NAME,'wd').send_keys("lo")
driver.find_element(By.CLASS_NAME,'s_ipt').send_keys('xxxfde')
driver.find_element(By.CSS_SELECTOR,'#kw').send_keys('zidonghua')
sleep()
