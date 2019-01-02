from calculator import *
from StartEnd import *


class Test_sub(Test_StartEnd):
    def test_sub(self):
        j = Math(10, 10)
        self.assertEqual(j.sub(), 0)

    def test_sub1(self):
        j = Math(7, 5)
        self.assertEqual(j.sub(), 2)
