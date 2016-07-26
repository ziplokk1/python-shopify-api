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

from shopify.products import Product


class TestProduct(TestCase):

    def setUp(self):
        with open(os.path.join(tests_, 'product.json'), 'rb') as f:
            self.data = json.loads(f.read())
        self.product = Product(self.data)

    def test_id(self):
        self.failUnlessEqual(self.data['id'], self.product.id)

    def test_title(self):
        self.failUnlessEqual(self.data['title'], self.product.title)

    def test_body_html(self):
        self.failUnlessEqual(self.data['body_html'], self.product.body_html)

    def test_vendor(self):
        self.failUnlessEqual(self.data['vendor'], self.product.vendor)

    def test_product_type(self):
        self.failUnlessEqual(self.data['product_type'], self.product.product_type)

    def _compare_dt(self, og_dt_key, dt2):
        og = self.data[og_dt_key].rpartition('-')[0]  # Remove the utc offset from the end of the timestamp
        og_dt = datetime.datetime.strptime(og, '%Y-%m-%dT%H:%M:%S')
        psr_dt = dt2.replace(tzinfo=None)
        self.failUnlessEqual(og_dt, psr_dt)

    def test_created_at(self):
        self._compare_dt('created_at', self.product.created_at)

    def test_handle(self):
        self.failUnlessEqual(self.data['handle'], self.product.handle)

    def test_updated_at(self):
        self._compare_dt('updated_at', self.product.updated_at)

    def test_published_at(self):
        self._compare_dt('published_at', self.product.published_at)

    def test_template_suffix(self):
        self.failUnlessEqual(self.data['template_suffix'], self.product.template_suffix)

    def test_published_scope(self):
        self.failUnlessEqual(self.data['published_scope'], self.product.published_scope)

    def test_tags(self):
        self.failUnlessEqual(self.data['tags'], self.product.tags)


if __name__ == '__main__':
    import unittest
    unittest.main()
