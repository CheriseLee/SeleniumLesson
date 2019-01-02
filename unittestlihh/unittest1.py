from testcase_manager.calculator import Math
import unittest


class TestMath(unittest.TestCase):
    def setUp(self):
        print("Start test")

    def test_add(self):
        j = Math(5, 10)
        self.assertNotEqual(j.add(), 10)

    def test_assertTrue(self):
        j = Math(5, 10)
        self.assertTrue(j.add() > 10)

    def test_assertIs(self):
        self.assertIs("51zxw", '51zxw')

    def aassertIn(self):
        self.assertIn("51zxw", "hello,51zxw")
        # self.assertIn("999", "hello,51zxw")

    def tearDown(self):
        print("Test end")
