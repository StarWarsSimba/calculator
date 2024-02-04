"""Unit tests for expr.py"""

import unittest
from expr import *

class TestIntConst(unittest.TestCase):

    def test_eval(self):
        five = IntConst(5)
        self.assertEqual(five.eval(),IntConst(5))

    def test_str(self):
        twelve = IntConst(12)
        self.assertEqual(str(twelve), "12")

    def test_repr(self):
        forty_two = IntConst(42)
        self.assertEqual(repr(forty_two), f"IntConst(42)")

if __name__ == "__main__":
    unittest.main()