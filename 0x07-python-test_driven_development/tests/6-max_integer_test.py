#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_value(self):
        """ checks the output for normal usage """

        self.assertAlmostEqual(max_integer([1, 2, 3, 5, -1]), 5)
        self.assertAlmostEqual(max_integer([-1, -2, -3, -5, -4]), -1)
        self.assertAlmostEqual(max_integer([0, 0, -1, 1, 100, -100]), 100)
        self.assertAlmostEqual(max_integer([]), None)
    
    def test_type(self):
        """ checks for the type passed to the function """

        self.assertRaises(KeyError, max_integer, {1: 3, 2: 5, 3: 7})
    
if __name__ == '__main__':
    unittest.main()