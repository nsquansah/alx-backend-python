#!/usr/bin/env python3
"""Module to test the @utils.py module"""
from parameterized import parameterized
from typing import (Dict, Tuple)
from unittest import (mock, TestCase)

from utils import (access_nested_map, get_json, memoize)


class TestAccessNestedMap(TestCase):
    """
    Subclass of unittest.TestCase for testing the @utils.access_nested_map
    function.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a"), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple,
            expected: int):
        """
        Checks that @utils.access_nested_map function returns expected result.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a")),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Dict, path: Tuple):
        """
        Tests @utils.access_nested_map function raises a KeyError when a
        key isn't found.
        """
        self.assertRaises(KeyError, access_nested_map, nested_map, path)


class TestGetJson(TestCase):
    """Tests the @utils.get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @mock.patch("utils.requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """Tests that @utils.get_json function returns the correct data"""
        mock_get.return_value.json.return_value = test_payload
        self.assertEqual(get_json(test_url), test_payload)

        mock_get.assert_called_once_with(test_url)


class TestMemoize(TestCase):
    """Tests the @utils.memoize function"""

    def test_memoize(self):
        """Tests the @utils.memoize function"""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        @mock.patch("TestClass.a_method")
        def t_memoize(self, mock_method):
            expected = 42
            mock_method.return_value = expected
            self.assertEqual(TestClass.a_property(), expected)
            self.assertEqual(TestClass.a_property(), expected)

            mock_method.assert_called_once()
