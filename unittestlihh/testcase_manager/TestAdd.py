from calculator import *
from StartEnd import *


class Test_add(Test_StartEnd):
    def test_add(self):
        j = Math(5, 10)
        self.assertNotEqual(j.add(), 10)

    def test_add1(self):
        j = Math(5, 5)
        self.assertEqual(j.add(), 10)
