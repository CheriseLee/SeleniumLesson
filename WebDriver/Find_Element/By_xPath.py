from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()

driver.get("http://www.baidu.com")
#右键前段html代码行，右键xpath可获得控件绝对路径,//表示在当前页面查找
#driver.find_element_by_xpath("").send_keys("Selenium")
#定位到input标签中ID为kw的元素
#driver.find_element_by_xpath("//input[@id='kw']").send_keys("Selenium")
#定位到input标签中name为wd的元素
#driver.find_element_by_xpath("//input[@name='wd']").send_keys("Selenium")

#定位所有标签元素中class属性为s_ipt的元素
driver.find_element_by_xpath("//*[@class='s_ipt']").send_keys("Selenium")
sleep(3)
driver.quit()