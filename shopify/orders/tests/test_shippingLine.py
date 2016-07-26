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

from shopify.orders import ShippingLine


class TestShippingLine(TestCase):

    def setUp(self):
        with open(os.path.join(tests_, 'shipping_line.json'), 'rb') as f:
            self.data = json.load(f)
        self.shipping_line = ShippingLine(self.data)

    def test_title(self):
        self.failUnlessEqual(self.data['title'], self.shipping_line.title)

    def test_price(self):
        self.failUnlessEqual(float(self.data['price']), self.shipping_line.price)

    def test_code(self):
        self.failUnlessEqual(self.data['code'], self.shipping_line.code)

    def test_source(self):
        self.failUnlessEqual(self.data['source'], self.shipping_line.source)

    def test_phone(self):
        self.failUnlessEqual(self.data['phone'], self.shipping_line.phone)

    def test_requested_fulfillment_service_id(self):
        self.failUnlessEqual(self.data['requested_fulfillment_service_id'], self.shipping_line.requested_fulfillment_service_id)

    def test_delivery_category(self):
        self.failUnlessEqual(self.data['delivery_category'], self.shipping_line.delivery_category)

    def test_carrier_identifier(self):
        self.failUnlessEqual(self.data['carrier_identifier'], self.shipping_line.carrier_identifier)


if __name__ == '__main__':
    import unittest
    unittest.main()
