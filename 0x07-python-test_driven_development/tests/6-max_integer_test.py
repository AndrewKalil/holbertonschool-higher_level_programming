#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class Test_max_integer(unittest.TestCase):
    """Test for max_integer([])

    Arguments:
        unittest {module} -- module containing test tool for python
    """
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 9, 99, 11, 0]), 99)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -55, -5, -3, -11]), -1)

    def test_what_about_zero(self):
        self.assertEqual(max_integer([-23, -25, -9, -1, 0]), 0)

    def test_mixed(self):
        self.assertEqual(max_integer([-100, -50, 0, 50, 100]), 100)

    def test_characters(self):
        self.assertEqual(max_integer(["j", "z", "a", "l"]), "z")

    def test_string(self):
        self.assertEqual(max_integer(["abcd", "bcde"]), "bcde")

    def test_bool(self):
        self.assertEqual(max_integer([True, False]), True)

    def test_types(self):
        self.assertRaises(TypeError, max_integer, [3, 5, "string"])
