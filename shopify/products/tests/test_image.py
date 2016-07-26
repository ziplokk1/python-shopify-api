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

from shopify.products import Image


class TestImage(TestCase):

    def setUp(self):
        with open(os.path.join(tests_, 'image.json'), 'rb') as f:
            self.data = json.loads(f.read())
        self.image = Image(self.data)

    def test_id(self):
        self.failUnlessEqual(self.data['id'], self.image.id)

    def test_product_id(self):
        self.failUnlessEqual(self.data['product_id'], self.image.product_id)

    def test_position(self):
        self.failUnlessEqual(self.data['position'], self.image.position)

    def _compare_dt(self, og_dt_key, dt2):
        og = self.data[og_dt_key].rpartition('-')[0]  # Remove the utc offset from the end of the timestamp
        og_dt = datetime.datetime.strptime(og, '%Y-%m-%dT%H:%M:%S')
        psr_dt = dt2.replace(tzinfo=None)
        self.failUnlessEqual(og_dt, psr_dt)

    def test_created_at(self):
        self._compare_dt('created_at', self.image.created_at)

    def test_updated_at(self):
        self._compare_dt('updated_at', self.image.updated_at)

    def test_src(self):
        self.failUnlessEqual(self.data['src'], self.image.src)


if __name__ == '__main__':
    import unittest
    unittest.main()
