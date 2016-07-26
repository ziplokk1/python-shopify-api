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

from shopify.orders import PaymentDetail


class TestPaymentDetail(TestCase):

    def setUp(self):
        with open(os.path.join(tests_, 'payment_detail.json'), 'rb') as f:
            self.data = json.load(f)
        self.payment_detail = PaymentDetail(self.data)

    def test_credit_card_bin(self):
        self.failUnlessEqual(self.data['credit_card_bin'], self.payment_detail.credit_card_bin)

    def test_avs_result_code(self):
        self.failUnlessEqual(self.data['avs_result_code'], self.payment_detail.avs_result_code)

    def test_cvv_result_code(self):
        self.failUnlessEqual(self.data['cvv_result_code'], self.payment_detail.cvv_result_code)

    def test_credit_card_number(self):
        self.failUnlessEqual(self.data['credit_card_number'], self.payment_detail.credit_card_number)

    def test_credit_card_company(self):
        self.failUnlessEqual(self.data['credit_card_company'], self.payment_detail.credit_card_company)


if __name__ == '__main__':
    import unittest
    unittest.main()
