from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Firefox()
driver.get("http://www.baidu.com/")
driver.maximize_window()
sleep(2)
driver.find_element_by_css_selector("#kw").send_keys("python")
#获取搜索框元素对象
element=driver.find_element_by_css_selector("#kw")
#双击操作
ActionChains(driver).double_click(element).perform()
sleep(2)
#右击操作
ActionChains(driver).context_click(element).perform()
#悬停操作
sleep(2)
above=driver.find_element_by_css_selector(".pf")
ActionChains(driver).move_to_element(above).perform()