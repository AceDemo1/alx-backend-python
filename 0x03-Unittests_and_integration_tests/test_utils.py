#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, n_map, path, ex):
        """test"""
        self.assertEqual(access_nested_map(n_map, path), ex)
        
    @parameterized.expand([
        ({}, ("a",),
        ({"a": 1, ("a", "b"), )
        ])
    def test_access_nested_map_exception(self, , n_map, path):
        """raises"""
        with self.assertRaises(KeyError) as err:
            access_nested_map(n_map, path)

if __name__ == "__main__":
    unittest.main()
