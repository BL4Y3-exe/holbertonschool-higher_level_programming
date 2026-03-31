#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_normal_list(self):
        """Test with a normal list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        """Max value at the beginning"""
        self.assertEqual(max_integer([10, 2, 3, 4]), 10)

    def test_max_at_end(self):
        """Max value at the end"""
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)

    def test_single_element(self):
        """List with one element"""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """Empty list should return None"""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """List with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """List with positive and negative numbers"""
        self.assertEqual(max_integer([-10, 5, 3, -1]), 5)

    def test_same_numbers(self):
        """List with all elements equal"""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_large_list(self):
        """Large list"""
        self.assertEqual(max_integer(list(range(1000))), 999)
