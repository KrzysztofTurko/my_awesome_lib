import unittest
from my_awesome_lib.data_utils import list_to_dict, filter_data

class TestDataUtils(unittest.TestCase):

    def test_list_to_dict(self):
        keys = ['a', 'b', 'c']
        values = [1, 2, 3]
        expected = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual(list_to_dict(keys, values), expected)

    def test_list_to_dict_invalid_length(self):
        keys = ['a', 'b']
        values = [1, 2, 3]
        with self.assertRaises(ValueError):
            list_to_dict(keys, values)

    def test_filter_data(self):
        data = [1, 2, 3, 4, 5]
        condition = lambda x: x % 2 == 0
        expected = [2, 4]
        self.assertEqual(filter_data(data, condition), expected)