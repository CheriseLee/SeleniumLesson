from testcase_manager.calculator import *
import unittest


class Test_StartEnd(unittest.TestCase):#继承父类unittest.TestCase
    def setUp(self):
        print("start")

    def tearDown(self):
        print("Test end")


class Test_add(Test_StartEnd):
    def test_add(self):
        j = Math(5, 10)
        self.assertNotEqual(j.add(), 10)

    def test_add1(self):
        j = Math(5, 5)
        self.assertEqual(j.add(), 10)


class Test_sub(Test_StartEnd):
    def test_sub(self):
        j = Math(10, 10)
        self.assertEqual(j.sub(), 0)

    def test_sub1(self):
        j = Math(7, 5)
        self.assertEqual(j.sub(), 2)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Test_add("test_add"))
    suite.addTest(Test_add("test_add1"))
    suite.addTest(Test_sub("test_sub"))
    suite.addTest(Test_sub("test_sub1"))
# 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
