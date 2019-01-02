from selenium import webdriver
from time import sleep
#不推荐使用tag name 定位
driver=webdriver.Firefox()
driver.get("http://www.51zxw.net")
driver.maximize_window()
sleep(2)
#找到一个超链接名字叫登录的元素，精确匹配
driver.find_element_by_link_text("登录").click()
sleep(2)
#找到一个超链接名字包含叫登录的元素，模糊匹配
driver.find_element_by_partial_link_text("忘记").click()

sleep(2)
# driver.refresh()
# sleep(2)
# driver.back()
# sleep(2)
# driver.forward()
# sleep(2)
# driver.quit()