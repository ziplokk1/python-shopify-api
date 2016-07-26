import json
import os
import sys
import datetime

from unittest import TestCase

# Prevent relative import errors
file_ = os.path.abspath(__file__)
tests_ = os.path.dirname(file_)
products_ = os.path.dirname(tests_)
shopify_ = os.path.dirname(products_)
root = os.path.dirname(shopify_)
sys.path.append(root)

from shopify.orders import ClientDetail


class TestClientDetail(TestCase):

    def setUp(self):
        with open(os.path.join(tests_, 'client_detail.json'), 'rb') as f:
            self.data = json.load(f)
        self.client_detail = ClientDetail(self.data)

    def test_browser_ip(self):
        self.failUnlessEqual(self.data['browser_ip'], self.client_detail.browser_ip)

    def test_accept_language(self):
        self.failUnlessEqual(self.data['accept_language'], self.client_detail.accept_language)

    def test_user_agent(self):
        self.failUnlessEqual(self.data['user_agent'], self.client_detail.user_agent)

    def test_session_hash(self):
        self.failUnlessEqual(self.data['session_hash'], self.client_detail.session_hash)

    def test_browser_width(self):
        self.failUnlessEqual(self.data['browser_width'], self.client_detail.browser_width)

    def test_browser_height(self):
        self.failUnlessEqual(self.data['browser_height'], self.client_detail.browser_height)


if __name__ == '__main__':
    import unittest
    unittest.main()
