import json
import os
import sys

from unittest import TestCase

# Prevent relative import errors
file_ = os.path.abspath(__file__)
tests_ = os.path.dirname(file_)
products_ = os.path.dirname(tests_)
shopify_ = os.path.dirname(products_)
root = os.path.dirname(shopify_)
sys.path.append(root)

from shopify.products import Option


class TestOption(TestCase):

    def setUp(self):
        with open(os.path.join(tests_, 'option.json'), 'rb') as f:
            self.data = json.loads(f.read())
        self.option = Option(self.data)

    def test_id(self):
        self.failUnlessEqual(self.data['id'], self.option.id)

    def test_product_id(self):
        self.failUnlessEqual(self.data['product_id'], self.option.product_id)

    def test_name(self):
        self.failUnlessEqual(self.data['name'], self.option.name)

    def test_position(self):
        self.failUnlessEqual(self.data['position'], self.option.position)

    def test_values(self):
        self.failUnlessEqual(self.data['values'], self.option.values)


if __name__ == '__main__':
    import unittest
    unittest.main()
