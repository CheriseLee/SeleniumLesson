import unittest


class Test_StartEnd(unittest.TestCase):#继承父类unittest.TestCase
    def setUp(self):
        print("start")

    def tearDown(self):
        print("Test end")


class Test_add(Test_StartEnd):
    def test_c(self):
        print("test_c")

    def test_b(self):
        print("test_b")


class Test_sub(Test_StartEnd):
    def test_d(self):
        print("test_d")

    def test_a(self):
        print("test_a")


if __name__ == '__main__':
    # suite = unittest.TestSuite()
    # suite.addTest(Test_add("test_add"))
    # suite.addTest(Test_add("test_add1"))
    # suite.addTest(Test_sub("test_sub"))
    # suite.addTest(Test_sub("test_sub1"))
# 执行测试
#     runner = unittest.TextTestRunner()
#     runner.run(suite)
    unittest.main()
