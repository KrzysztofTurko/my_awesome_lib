import unittest
from my_awesome_lib.text_processing import reverse_text, remove_duplicates

class TestTextProcessing(unittest.TestCase):

    def test_reverse_text(self):
        self.assertEqual(reverse_text("hello"), "olleh")

    def test_remove_duplicates(self):
        words = ["apple", "banana", "apple", "orange"]
        expected = ["apple", "banana", "orange"]
        self.assertEqual(sorted(remove_duplicates(words)), sorted(expected))