from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.maximize_window()
sleep(2)
#根据id定位，在id前面加#表示按id定位
driver.find_element_by_css_selector("#kw").send_keys("我要自学网")
#根据class定位，在class值前面加.表示按class定位
driver.find_element_by_css_selector(".s_ipt").send_keys("python")
#根据属性定位，在id前面加#表示按id定位
driver.find_element_by_css_selector("[autocomplete=off]").send_keys("selenium")
#根据元素层级定位 form是标签，.fm表示form对应的class是fm,>表示路径
driver.find_element_by_css_selector("form.fm>span>input").send_keys("welcome")
