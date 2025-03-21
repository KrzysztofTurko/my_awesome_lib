import unittest
from my_awesome_lib.math_tools import add_numbers

class TestMathTools(unittest.TestCase):
    def test_add_numbers_positive(self):
        # Test dodawania liczb dodatnich
        self.assertEqual(add_numbers(2, 3), 5)

    def test_add_numbers_negative(self):
        # Test dodawania liczb ujemnych
        self.assertEqual(add_numbers(-1, -1), -2)

    def test_add_numbers_mixed(self):
        # Test dodawania liczby dodatniej i ujemnej
        self.assertEqual(add_numbers(5, -3), 2)

    def test_add_numbers_zero(self):
        # Test dodawania z zerem
        self.assertEqual(add_numbers(0, 0), 0)
        self.assertEqual(add_numbers(5, 0), 5)

if __name__ == "__main__":
    unittest.main()