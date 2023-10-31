#!/usr/bin/python3
"""
Module that contains unit test for max_integer function.
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Test class for max_integer.
    """

    def test_normal(self):
        """
        Test with a normal list of ints: should return the max result.
        """

        test_list = [1, 2, 3, 4, 5]
        result = max_integer(test_list)
        self.assertEqual(result, 5)

    def test_mixed(self):
        """
        Test with a list of mixed types: should raise a TypeError exception.
        """

        test_list = ["a", "b", 9, "c"]
        self.assertRaises(TypeError, max_integer, test_list)

    def test_empty(self):
        """
        Test with an empty list: should return None.
        """

        test_list = []
        result = max_integer(test_list)
        self.assertEqual(result, None)

    def test_negative(self):
        """
        Test with a list of negative values: should return the max.
        """

        test_list = [-20, -5, -1]
        result = max_integer(test_list)
        self.assertEqual(result, -1)

    def test_float(self):
        """
        Test with list of mixed ints and floats: should return the max.
        """

        test_list = [3, 9.5, 2]
        result = max_integer(test_list)
        self.assertEqual(result, 9.5)

    def test_not_list(self):
        """
        Test with parameter that's not a list: should raise a TypeError.
        """

        self.assertRaises(TypeError, max_integer, 14)

    def test_singleton(self):
        """
        Test with list of one int: should return the value of this int.
        """

        test_list = [99]
        result = max_integer(test_list)
        self.assertEqual(result, 99)

    def test_duplicate(self):
        """
        Test with list of duplicate values: should return the value.
        """

        test_list = [8, 8, 8, 8, 8]
        result = max_integer(test_list)
        self.assertEqual(result, 8)

    def test_string(self):
        """
        Test with list of strings: should return the first string.
        """

        test_list = ["hey", "hello"]
        result = max_integer(test_list)
        self.assertEqual(result, "hey")

    def test_none(self):
        """
        Test with None as parameter: should raise a TypeError.
        """

        self.assertRaises(TypeError, max_integer, None)


if __name__ == '__main__':
    unittest.main()
