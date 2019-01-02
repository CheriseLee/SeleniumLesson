import unittest


class Test_StartEnd(unittest.TestCase):#继承父类unittest.TestCase
    def setUp(self):
        print("start")

    def tearDown(self):
        print("Test end")


#@unittest.skip("skip Test_add")#括号中是跳过的原因，跳过接下来这个类，里面所有方法
class Test_add(Test_StartEnd):
    @classmethod
    def setUpClass(cls):#针对测试类的操作,和@classmethod一起出现
        print("Class module start")

    @classmethod
    def tearDownClass(cls):
        print("Class module tearDown")

    def test_c(self):
        print("test_c")
    #@unittest.expectedFailure
    def test_b(self):
        print("test_b")


class Test_sub(Test_StartEnd):
    def test_d(self):
        print("test_d")

    @unittest.skipIf(4>3, "skip")#跳过接下来这一个方法
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
