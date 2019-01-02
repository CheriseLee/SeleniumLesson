from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import ctime
from time import sleep


class Login():
    def user_login(self, driver):
        # 输入用户名
        driver.find_element_by_name('username').clear()
        driver.find_element_by_name('username').send_keys('51zxw')
        # 输入密码
        driver.find_element_by_name('password').clear()
        driver.find_element_by_name('password').send_keys('1234567890')

        driver.find_element_by_name('Submit').click()

    def user_logout(self,driver):
        driver.implicitly_wait(5)
        try:
            print(ctime())
            driver.find_element_by_link_text('退出').click()
        except NoSuchElementException as msg:
            print(msg)
        finally:
            print(ctime())
        driver.switch_to.alert.accept()


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1")
    driver.maximize_window()
    driver.implicitly_wait(2)
    Login().user_login(driver)
    Login().user_logout(driver)
