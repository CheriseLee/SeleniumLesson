import unittest
from model import function,myunit
from page_object.LoginPage import *
from time import sleep

#用户名正确密码正确登录
class LoginTest(myunit.StartEnd):
    # 用户名正确密码正确登录
    def test_login1_normal(self):
        print('test login1_ normal is start run...')
        po = LoginPage(self.driver)
        po.Login_action('51zxw',123456)
        sleep(3)

        #断言与截屏
        self.assertEqual(po.type_loginPass_hint(),'我的空间')
        function.insert_img(self.driver,"51zxw_login1_normal.png")
        print("test_login1_normal is test end!")

     # 用户名正确密码错误
    def test_login1_normal(self):
        'username is ok,password is error'
        print('test login2_pawwordError is start run...')
        po = LoginPage(self.driver)
        po.Login_action('51zxw', 123454)
        sleep(3)

        # 断言与截屏
        self.assertEqual(po.type_loginFail_hint(), '')
        function.insert_img(self.driver, "51zxw_login2_fail.png")
        print("test_login2_passwordError is test end!")

    def test_login3_empty(self):
        '''username and password is empty'''
        print('test login3_empty is start run...')
        po = LoginPage(self.driver)
        po.Login_action('', '')
        sleep(3)

        # 断言与截屏
        self.assertEqual(po.type_loginFail_hint(), '')
        function.insert_img(self.driver, "51zxw_login3_empty.png")
        print("test_login3_empty is test end!")

if __name__ == '__main__':
    unittest.main()
