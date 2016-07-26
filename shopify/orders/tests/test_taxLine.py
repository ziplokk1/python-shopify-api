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

from shopify.orders import TaxLine


class TestTaxLine(TestCase):

    def setUp(self):
        with open(os.path.join(tests_, 'tax_line.json'), 'rb') as f:
            self.data = json.load(f)
        self.tax_line = TaxLine(self.data)

    def test_title(self):
        self.failUnlessEqual(self.data['title'], self.tax_line.title)

    def test_price(self):
        self.failUnlessEqual(float(self.data['price']), self.tax_line.price)

    def test_rate(self):
        self.failUnlessEqual(self.data['rate'], self.tax_line.rate)


if __name__ == '__main__':
    import unittest
    unittest.main()
