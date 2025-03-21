import unittest
from my_awesome_lib.data_utils import convert_to_int

class TestDataUtils(unittest.TestCase):
    def test_convert_to_int_valid(self):
        # Test poprawnej konwersji
        self.assertEqual(convert_to_int(["1", "2", "3"]), [1, 2, 3])

    def test_convert_to_int_invalid(self):
        # Test niepoprawnej konwersji (powinien zgłosić ValueError)
        with self.assertRaises(ValueError):
            convert_to_int(["1", "abc", "3"])

    def test_convert_to_int_empty(self):
        # Test pustej listy
        self.assertEqual(convert_to_int([]), [])

if __name__ == "__main__":
    unittest.main()