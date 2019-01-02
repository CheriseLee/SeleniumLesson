from selenium import webdriver
from time import sleep
#不推荐使用tag name 定位
driver=webdriver.Firefox()
driver.get("http://www.51zxw.net")
driver.maximize_window()
sleep(2)
driver.find_element_by_id("frm_login_url").click()
sleep(2)
#获取当前页面第一个标签为input的元素
#driver.find_element_by_tag_name("input").send_keys("463836190@qq.com")
#获取当前页面所有标签为input的元素
driver.find_element_by_id("loginStr").send_keys("463836190@qq.com")
sleep(2)
driver.find_element_by_id("pwd").send_keys("870727")
sleep(2)
driver.find_element_by_link_text("登录").click()
sleep(2)
# driver.refresh()
# sleep(2)
# driver.back()
# sleep(2)
# driver.forward()
# sleep(2)
# driver.quit()