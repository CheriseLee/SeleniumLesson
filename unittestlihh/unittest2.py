from unittest1 import *
import unittest


if __name__ == '__main__':

    # unittest.main()
    #构造测试集
    suite = unittest.TestSuite()
    suite.addTest(TestMath("test_add"))
    suite.addTest(TestMath("aassertIn"))

# 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
