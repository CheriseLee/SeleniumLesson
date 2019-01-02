from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.maximize_window()
sleep(2)
#driver.find_element_by_id("kw").send_keys("我要自学网")
driver.find_element_by_name("wd").send_keys("我要自学网")
driver.find_element_by_id("su").click()
# driver.find_element_by_id("su").click()
sleep(2)
# driver.refresh()
# sleep(2)
# driver.back()
# sleep(2)
# driver.forward()
# sleep(2)
driver.quit()