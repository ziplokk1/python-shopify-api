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

from shopify.products import Variant


class TestVariant(TestCase):

    def _compare_dt(self, og_dt_key, dt2):
        og = self.data[og_dt_key].rpartition('-')[0]  # Remove the utc offset from the end of the timestamp
        og_dt = datetime.datetime.strptime(og, '%Y-%m-%dT%H:%M:%S')
        psr_dt = dt2.replace(tzinfo=None)
        self.failUnlessEqual(og_dt, psr_dt)

    def setUp(self):
        with open(os.path.join(tests_, 'variant.json'), 'rb') as f:
            self.data = json.loads(f.read())
        self.variant = Variant(self.data)

    def test_id(self):
        self.failUnlessEqual(self.data['id'], self.variant.id)

    def test_product_id(self):
        self.failUnlessEqual(self.data['product_id'], self.variant.product_id)

    def test_title(self):
        self.failUnlessEqual(self.data['title'], self.variant.title)

    def test_price(self):
        self.failUnlessEqual(float(self.data['price']), self.variant.price)

    def test_sku(self):
        self.failUnlessEqual(self.data['sku'], self.variant.sku)

    def test_position(self):
        self.failUnlessEqual(self.data['position'], self.variant.position)

    def test_grams(self):
        self.failUnlessEqual(self.data['grams'], self.variant.grams)

    def test_inventory_policy(self):
        self.failUnlessEqual(self.data['inventory_policy'], self.variant.inventory_policy)

    def test_compare_at_price(self):
        self.failUnlessEqual(self.data['compare_at_price'], self.variant.compare_at_price)

    def test_fulfillment_service(self):
        self.failUnlessEqual(self.data['fulfillment_service'], self.variant.fulfillment_service)

    def test_inventory_management(self):
        self.failUnlessEqual(self.data['inventory_management'], self.variant.inventory_management)

    def test_option_1(self):
        self.failUnlessEqual(self.data['option1'], self.variant.option_1)

    def test_option_2(self):
        self.failUnlessEqual(self.data['option2'], self.variant.option_2)

    def test_option_3(self):
        self.failUnlessEqual(self.data['option3'], self.variant.option_3)

    def test_created_at(self):
        self._compare_dt('created_at', self.variant.created_at)

    def test_updated_at(self):
        self._compare_dt('updated_at', self.variant.updated_at)

    def test_taxable(self):
        self.failUnlessEqual(self.data['taxable'], self.variant.taxable)

    def test_barcode(self):
        self.failUnlessEqual(self.data['barcode'], self.variant.barcode)

    def test_image_id(self):
        self.failUnlessEqual(self.data['image_id'], self.variant.image_id)

    def test_inventory_quantity(self):
        self.failUnlessEqual(self.data['inventory_quantity'], self.variant.inventory_quantity)

    def test_weight(self):
        self.failUnlessEqual(self.data['weight'], self.variant.weight)

    def test_weight_unit(self):
        self.failUnlessEqual(self.data['weight_unit'], self.variant.weight_unit)

    def test_old_inventory_quantity(self):
        self.failUnlessEqual(self.data['old_inventory_quantity'], self.variant.old_inventory_quantity)

    def test_requires_shipping(self):
        self.failUnlessEqual(self.data['requires_shipping'], self.variant.requires_shipping)


if __name__ == '__main__':
    import unittest
    unittest.main()
