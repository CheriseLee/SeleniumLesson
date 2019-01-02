from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
driver=webdriver.Firefox()
driver.get("http://www.baidu.com/")
driver.maximize_window()
sleep(2)
driver.find_element_by_css_selector("#kw").send_keys("python")
#键盘全选操作CTRL+A
driver.find_element_by_css_selector("#kw").send_keys(Keys.CONTROL,'a')
#键盘全选操作CTRL+C
driver.find_element_by_css_selector("#kw").send_keys(Keys.CONTROL,'c')
sleep(2)
#打开搜狗
driver.get("http://www.sogou.com/")
sleep(2)
driver.find_element_by_css_selector("#query").send_keys(Keys.CONTROL,'V')