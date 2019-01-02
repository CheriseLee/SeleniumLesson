from data import *


driver = webdriver.Firefox()
driver.get("http://127.0.0.1")
driver.maximize_window()
Login().user_login(driver, '51zxw', '1234567890')
Login().user_logout(driver)
