from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
#当按照class name 等属性找不到，或者找到的结果不唯一时//元素向上找，找到有class id属性为止
#层级和属性结合定位
driver.find_element_by_xpath("//form[@id='form']/span/input").send_keys("my name")
#逻辑运算组合定位
driver.find_element_by_xpath("//input[@id='kw' and@class='s_ipt']").send_keys("my name2")