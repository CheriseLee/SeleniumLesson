from selenium import webdriver
from time import sleep
import os

def login():
    driver = webdriver.Firefox()
    driver.get("http://120.78.72.58:10086/")
    driver.find_element_by_id("username").send_keys("liuyx")
    driver.find_element_by_id("password").send_keys("123123")
    driver.find_element_by_class_name("loginbtn").click()
    sleep(2)
    driver.refresh()

if __name__ == '__main__':
    login()


    #driver.quit()