from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()

driver.get("http://www.51zxw.net")
#通过linktext传值,精确匹配
driver.find_element_by_link_text("程序开发").click()
#通过linktext传值,模糊匹配匹配
driver.find_element_by_partial_link_text("神秘面纱").click()
sleep(2)

driver.quit()