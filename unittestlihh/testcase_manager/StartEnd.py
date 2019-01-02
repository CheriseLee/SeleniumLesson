import unittest


class Test_StartEnd(unittest.TestCase):#继承父类unittest.TestCase
    def setUp(self):
        print("start")

    def tearDown(self):
        print("Test end")
