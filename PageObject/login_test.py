from LoginPage import *
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()

username = '51zxw'
password = '123456'
test_user_login(driver, username, password)
sleep(2)
