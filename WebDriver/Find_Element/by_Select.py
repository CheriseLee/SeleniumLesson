from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select

driver=webdriver.Firefox()
driver.get("http://www.bigear.cn/")
driver.maximize_window()
sleep(2)
#根据select类来定位
select=Select(driver.find_element_by_css_selector("[onchange='showBroadcastInfo(this.value)']"))
select.select_by_value("latestvoaspecial")
print("sta")
sleep(2)
select.select_by_visible_text("VOA News")
print("sta1")