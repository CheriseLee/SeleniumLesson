from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://www.51zxw.com")
driver.maximize_window()
sleep(2)
driver.get("http://www.51zxw.net/list.aspx?page=2&cid=615")
driver.set_window_size(400,400)
driver.refresh()
sleep(2)
driver.back()
sleep(2)
driver.forward()
sleep(2)
driver.quit()