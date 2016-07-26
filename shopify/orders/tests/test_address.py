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

from shopify.orders import Address


class TestAddress(TestCase):

    def setUp(self):
        with open(os.path.join(tests_, 'address.json'), 'rb') as f:
            self.data = json.load(f)
        self.address = Address(self.data)

    def test_first_name(self):
        self.failUnlessEqual(self.data['first_name'], self.address.first_name)

    def test_address_1(self):
        self.failUnlessEqual(self.data['address1'], self.address.address_1)

    def test_phone(self):
        self.failUnlessEqual(self.data['phone'], self.address.phone)

    def test_city(self):
        self.failUnlessEqual(self.data['city'], self.address.city)

    def test_zip(self):
        self.failUnlessEqual(self.data['zip'], self.address.zip)

    def test_province(self):
        self.failUnlessEqual(self.data['province'], self.address.province)

    def test_country(self):
        self.failUnlessEqual(self.data['country'], self.address.country)

    def test_last_name(self):
        self.failUnlessEqual(self.data['last_name'], self.address.last_name)

    def test_address_2(self):
        self.failUnlessEqual(self.data['address2'], self.address.address_2)

    def test_company(self):
        self.failUnlessEqual(self.data['company'], self.address.company)

    def test_longitude(self):
        self.failUnlessEqual(self.data['latitude'], self.address.latitude)

    def test_latitude(self):
        self.failUnlessEqual(self.data['longitude'], self.address.longitude)

    def test_country_code(self):
        self.failUnlessEqual(self.data['country_code'], self.address.country_code)

    def test_province_code(self):
        self.failUnlessEqual(self.data['province_code'], self.address.province_code)


if __name__ == '__main__':
    import unittest
    unittest.main()
