from selenium import webdriver
import unittest
from time import sleep


class TestBaidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(2)
        self.driver.get("http://www.baidu.com")
        self.driver.maximize_window()

    def test_baidu(self):
        driver = self.driver

        driver.find_element_by_css_selector('#kw').send_keys("我要自学网")
        sleep(3)
        driver.find_element_by_css_selector('#su').click()
        sleep(3)

        title = driver.title
        self.assertEqual(title, "我要自学网_百度搜索")

    def tearDown(self):
        self.driver.quit()

