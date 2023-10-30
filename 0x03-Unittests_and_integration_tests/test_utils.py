#!/usr/bin/env python3
"""
Module for unittest using parameterized
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Class for unittest case
    """
    @parameterized.expand({
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    })
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Method to test nexted map function
        """
        result = access_nexted_map(nested_map, path)
        self.assertEqual(result, expected)


if __name__ =="__main__":
    unittest.main()
