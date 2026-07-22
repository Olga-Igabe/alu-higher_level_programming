#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for the max_integer function."""

    def test_empty_list(self):
        """An empty list returns None."""
        self.assertEqual(max_integer([]), None)

    def test_default_argument(self):
        """No argument (default empty list) returns None."""
        self.assertEqual(max_integer(), None)

    def test_one_element(self):
        """A list with a single element returns that element."""
        self.assertEqual(max_integer([5]), 5)

    def test_max_at_start(self):
        """The max is correctly found when it's the first element."""
        self.assertEqual(max_integer([9, 1, 2, 3]), 9)

    def test_max_at_end(self):
        """The max is correctly found when it's the last element."""
        self.assertEqual(max_integer([1, 2, 3, 9]), 9)

    def test_max_in_middle(self):
        """The max is correctly found when it's in the middle."""
        self.assertEqual(max_integer([1, 9, 2, 3]), 9)

    def test_all_same_values(self):
        """A list where every element is identical."""
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)

    def test_negative_numbers(self):
        """A list of negative numbers."""
        self.assertEqual(max_integer([-5, -1, -9, -3]), -1)

    def test_mixed_positive_negative(self):
        """A list mixing positive and negative numbers."""
        self.assertEqual(max_integer([-5, 3, -9, 7, 0]), 7)

    def test_floats(self):
        """A list of floats."""
        self.assertEqual(max_integer([1.5, 2.7, 0.3]), 2.7)

    def test_duplicate_max_values(self):
        """The max value appears more than once."""
        self.assertEqual(max_integer([3, 9, 9, 2]), 9)


if __name__ == "__main__":
    unittest.main()
