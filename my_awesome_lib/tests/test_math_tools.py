import unittest
from my_awesome_lib.math_tools import calculate_average, factorial

class TestMathTools(unittest.TestCase):

    def test_calculate_average(self):
        numbers = [1, 2, 3, 4, 5]
        self.assertEqual(calculate_average(numbers), 3.0)

    def test_calculate_average_empty_list(self):
        with self.assertRaises(ValueError):
            calculate_average([])

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            factorial(-1)