#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_base(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_none(self):
        self.assertEqual(max_integer(), None)

if __name__ == '__main__':
    unittest.main()
