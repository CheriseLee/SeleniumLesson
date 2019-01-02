from selenium import webdriver
from time import sleep
from time import ctime
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.maximize_window()
sleep(2)
above=driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(above).perform()
driver.implicitly_wait(5)
driver.find_element_by_link_text('搜索设置').click()
driver.implicitly_wait(5)
driver.find_element_by_css_selector('.prefpanelgo').click()
driver.implicitly_wait(5)
driver.switch_to.alert.accept()
