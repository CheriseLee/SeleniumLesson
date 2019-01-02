from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.maximize_window()
#按照绝对路径去获取
# driver.find_element_by_xpath("")
#利用元素熟悉定位，定位到input标签中，id为kw的元素
driver.find_element_by_xpath("//input[@id='kw']").send_keys("my name")

#，定位到input标签中，name为wd的元素
driver.find_element_by_xpath("//input[@name='wd']").send_keys("my name2")

#，定位到所有标签中，class属性为s_ipt的元素
driver.find_element_by_xpath("//*[@class='s_ipt']").send_keys("my name3")
