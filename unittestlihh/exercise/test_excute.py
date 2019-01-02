import unittest
test_dir = './'#代表当前路径
discover = unittest.defaultTestLoader.discover(test_dir, pattern="exer*.py")

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(discover)
