from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://www.51zxw.net/list.aspx?cid=615")
driver.maximize_window()
sleep(2)
mainIndex=driver.current_window_handle
driver.find_element_by_partial_link_text('2-1').click()
sleep(2)
driver.switch_to.window(mainIndex)
driver.find_element_by_partial_link_text('3-1').click()
sleep(2)