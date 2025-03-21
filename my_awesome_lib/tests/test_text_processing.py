import unittest
from my_awesome_lib.text_processing import reverse_string

class TestTextProcessing(unittest.TestCase):
    def test_reverse_string_normal(self):
        # Test odwracania standardowego ciągu znaków
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_reverse_string_empty(self):
        # Test odwracania pustego ciągu znaków
        self.assertEqual(reverse_string(""), "")

    def test_reverse_string_special_chars(self):
        # Test odwracania ciągu ze znakami specjalnymi
        self.assertEqual(reverse_string("!@#"), "#@!")

    def test_reverse_string_spaces(self):
        # Test odwracania ciągu ze spacjami
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")

if __name__ == "__main__":
    unittest.main()