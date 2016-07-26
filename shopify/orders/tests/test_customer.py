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

from shopify.orders import Customer


class TestCustomer(TestCase):

    def setUp(self):
        with open(os.path.join(tests_, 'customer.json'), 'rb') as f:
            self.data = json.load(f)
        self.customer = Customer(self.data)

    def _compare_dt(self, og_dt_key, dt2):
        og = self.data[og_dt_key].rpartition('-')[0]  # Remove the utc offset from the end of the timestamp
        og_dt = datetime.datetime.strptime(og, '%Y-%m-%dT%H:%M:%S')
        psr_dt = dt2.replace(tzinfo=None)
        self.failUnlessEqual(og_dt, psr_dt)

    def test_id(self):
        self.failUnlessEqual(self.data['id'], self.customer.id)

    def test_email(self):
        self.failUnlessEqual(self.data['email'], self.customer.email)

    def test_accepts_marketing(self):
        self.failUnlessEqual(self.data['accepts_marketing'], self.customer.accepts_marketing)

    def test_created_at(self):
        self._compare_dt('created_at', self.customer.created_at)

    def test_updated_at(self):
        self._compare_dt('updated_at', self.customer.updated_at)

    def test_first_name(self):
        self.failUnlessEqual(self.data['first_name'], self.customer.first_name)

    def test_last_name(self):
        self.failUnlessEqual(self.data['last_name'], self.customer.last_name)

    def test_orders_count(self):
        self.failUnlessEqual(self.data['orders_count'], self.customer.orders_count)

    def test_state(self):
        self.failUnlessEqual(self.data['state'], self.customer.state)

    def test_total_spent(self):
        self.failUnlessEqual(float(self.data['total_spent']), self.customer.total_spent)

    def test_last_order_id(self):
        self.failUnlessEqual(self.data['last_order_id'], self.customer.last_order_id)

    def test_note(self):
        self.failUnlessEqual(self.data['note'], self.customer.note)

    def test_verified_email(self):
        self.failUnlessEqual(self.data['verified_email'], self.customer.verified_email)

    def test_multipass_identifier(self):
        self.failUnlessEqual(self.data['multipass_identifier'], self.customer.multipass_identifier)

    def test_tax_exempt(self):
        self.failUnlessEqual(self.data['tax_exempt'], self.customer.tax_exempt)

    def test_tags(self):
        self.failUnlessEqual(self.data['tags'], self.customer.tags)

    def test_last_order_name(self):
        self.failUnlessEqual(self.data['last_order_name'], self.customer.last_order_name)


if __name__ == '__main__':
    import unittest
    unittest.main()
