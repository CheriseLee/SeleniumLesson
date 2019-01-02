from selenium import webdriver
from time import sleep

#启动浏览器之前确保浏览器关闭，注意浏览器版本和selenium要配套
driver=webdriver.Firefox()
driver.maximize_window()
#driver=webdriver.Chrome()
#driver=webdriver.Ie()
#打开我要自学网
driver.get("http://www.51zxw.net/")
sleep(2)
driver.get("http://www.51zxw.net/show.aspx?id=60544&cid=615")
sleep(2)
#刷新页面
driver.refresh()
#设置窗口大小
driver.set_window_size(800,800)
sleep(2)
#撤销
driver.back()
sleep(2)
#重做
driver.forward()
sleep(2)
print(driver.title)
sleep(3)
#打开百度
driver.get("http://www.baidu.com")
print(driver.title)
sleep(2)

#退出浏览器
driver.quit()