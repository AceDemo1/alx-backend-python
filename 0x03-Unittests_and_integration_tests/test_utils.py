#!/usr/bin/env python3
import unittest
import requests
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize

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
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
        ])
    def test_access_nested_map_exception(self, n_map, path):
        """raises"""
        with self.assertRaises(KeyError) as err:
            access_nested_map(n_map, path)

class TestGetJson(unittest.TestCase):
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    @patch('requests.get')
    def test_get_json(self, url, response, mock_get):
        """mock"""
        mock_get.return_value.json.return_value = response
        self.assertEqual(mock_get(url), response)
        mock_get.assert_called_once_with(url)

class TestMemoize(unittest.TestCase):
    """def test_memoize(self):
        """'memoize'"""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()"""





if __name__ == "__main__":
    unittest.main()
