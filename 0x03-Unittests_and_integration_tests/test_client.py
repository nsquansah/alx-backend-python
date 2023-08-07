#!/usr/bin/env python3
"""Module to test the @client.py module"""
from client import GithubOrgClient
from parameterized import parameterized
from unittest import mock, TestCase
from unittest.mock import MagicMock


class TestGithubOrgClient(TestCase):
    """A subclass of @unittest.TestCase for testing the
    @client.GithubOrgClient function.
    """

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @mock.patch("client.get_json")
    def test_org(self, org, mock_method):
        """Tests the @GithubOrgClient.org method"""
        expected = {"payload": False}
        mock_method.return_value = MagicMock(return_value=expected)
        git_client = GithubOrgClient(org)
        org_data = git_client.org()
        self.assertEqual(org_data, expected)
        org_data = git_client.org()
        self.assertEqual(org_data, expected)

        mock_method.assert_called_once()
