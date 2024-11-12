#!/usr/bin/env python3
"""Test for A github org client
"""
import unittest
from client import GithubOrgClient
from unittest.mock import patch, PropertyMock
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """GithubOrgClient"""
    @parameterized.expand([
        ('google',),
        ('abc',)
    ])
    @patch('client.get_json')
    def test_org(self, name, mock_obj):
        """test_org"""
        mock_obj.return_value = {}
        res = GithubOrgClient(name).org
        mock_obj.assert_called_once_with(f"https://api.github.com/orgs/{name}")
        self.assertEqual(res, mock_obj.return_value)

    def test_public_repos_url(self):
        """public repos url"""
        with patch.object(GithubOrgClient,
                'org', new_callable=PropertyMock) as mock_obj:
            mock_obj.return_value = {}
            obj = GithubOrgClient('test')
            self.asserEqual(obj._public_repos_url, {})

    @patch('client.get_json')
    def test_public_repos(self, mock_get):
        """public repos"""
        mock_get.return_value = [{'name': 'law'}]
        with patch.object(GithubOrgClient,
                '_public_repos_url', new_callable=PropertyMock) as mock_obj:
            mock_obj.return_value = "https://api.github.com/orgs/test"
            obj = GithubOrgClient('test')
            self.assertEqual(obj.public_repos(), ['law'])
            mock_get.assert_called_once_with(mock_obj.return_value)
            mock_obj.assert_called_once()
