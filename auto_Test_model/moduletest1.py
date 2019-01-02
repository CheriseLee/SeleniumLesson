from moduletest import *

if __name__ == '__main__':

    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1")
    driver.maximize_window()
    Login().user_login(driver)
    Login().user_logout(driver)

