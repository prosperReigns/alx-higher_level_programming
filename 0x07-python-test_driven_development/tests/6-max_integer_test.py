#!/usr/bin/python3

import unittest
max_integer = __import__('6-max_integer').max_integer

class test_max_integer(unittest.TestCase):
    def test_list(self):
        if not isinstance(self, list):
            raise TypeError("value must be a list of integers")

    def test_max(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

if __name__ == "__main__":
    unittest.main()