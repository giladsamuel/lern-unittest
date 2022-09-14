import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        result = calc.add(5,10)
        self.assertEqual(result, 15)
