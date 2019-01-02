from selenium import webdriver
from time import sleep

def updateNormItem():
    driver = webdriver.Firefox()
    sleep(2)
    driver.find_element_by_class_name("m-xs").click()

if __name__ == '__main__':

    suite=unittest.TestSuite()
    suite.addTest(Test_add(""))


    runner=unittest.textTestRunner()
    runner.run(suite)


    driver = webdriver.Firefox()
    sleep(2)
    driver.find_element_by_class_name("m-xs").click()