from testcase_manager.calculator import Math
import unittest


class Test_add(unittest.TestCase):
    def setUp(self):
        print("start")

    def test_add(self):
        j = Math(5, 10)
        self.assertNotEqual(j.add(), 10)

    def test_add1(self):
        j = Math(5, 5)
        self.assertEqual(j.add(), 10)

    def tearDown(self):
        print("Test end")


class Test_sub(unittest.TestCase):
    def setUp(self):
        print("start")

    def test_sub(self):
        j = Math(10, 10)
        self.assertEqual(j.sub(), 0)

    def test_sub1(self):
        j = Math(7, 5)
        self.assertEqual(j.sub(), 2)

    def tearDown(self):
        print("Test end")


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Test_add("test_add"))
    suite.addTest(Test_add("test_add1"))
    suite.addTest(Test_sub("test_sub"))
    suite.addTest(Test_sub("test_sub1"))
# 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
