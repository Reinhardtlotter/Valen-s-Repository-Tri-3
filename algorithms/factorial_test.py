from unittest import TestCase
from factorial import Factor
import math

class TestFactorial(TestCase):
    def test_factorials (self):
        self.assertEqual (Factor.factorial(5), 120)
        self.assertEqual (Factor.factorial(4), 24)
        self.assertEqual (Factor.factorial(0), 1)
        self.assertEqual (Factor.factorial(1), 1)
 
    def test_negative_factor (self):
        self.assertTrue(math.isnan(Factor.factorial(-1)))