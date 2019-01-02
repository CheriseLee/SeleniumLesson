from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()

# driver.get("http://www.baidu.com")
#通过ID定位
#driver.find_element_by_css_selector("#kw").send_keys("我要自学网")
#通过Class定位
# driver.find_element_by_css_selector(".s_ipt").send_keys("我要自学网")
#通过属性定位
# driver.find_element_by_css_selector("[autocomplete='off']").send_keys("我要自学网")
# sleep(2)
# driver.find_element_by_id("su").click()
# sleep(2)

driver.get("http://www.51zxw.net")
driver.find_element_by_css_selector("form#loginForm>ul>input").send_keys("test")
sleep(2)
driver.find_element_by_css_selector("form#loginForm>ul>input[type='password']").send_keys("test")
sleep(2)