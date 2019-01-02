from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()

driver.get("http://www.baidu.com")
#通过ID传值
driver.find_element_by_class_name("s_ipt").send_keys("Selenium我要自学网")
#通过name传值
#driver.find_element_by_name("wd").send_keys("Selenium我要自学网")
#driver.get("http://www.51zxw.net")
sleep(2)
#driver.find_element_by_id("su").click()
#sleep(3)

driver.quit()