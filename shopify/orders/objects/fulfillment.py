from ...base import BaseParser, string_to_datetime
from .line_item import LineItem


class Receipt(BaseParser):

    @property
    def testcase(self):
        return self._dict.get('testcase')

    @property
    def authorization(self):
        return self._dict.get('authorization')


class Fulfillment(BaseParser):

    @property
    def order_id(self):
        return self._dict.get('order_id')

    @property
    def status(self):
        return self._dict.get('status')

    @property
    def created_at(self):
        return string_to_datetime(self._dict.get('created_at'))

    @property
    def service(self):
        return self._dict.get('service')

    @property
    def updated_at(self):
        return string_to_datetime(self._dict.get('updated_at'))

    @property
    def tracking_company(self):
        return self._dict.get('tracking_company')

    @property
    def shipment_status(self):
        return self._dict.get('shipment_status')

    @property
    def tracking_number(self):
        return self._dict.get('tracking_number')

    @property
    def tracking_numbers(self):
        return self._dict.get('tracking_numbers')

    @property
    def tracking_url(self):
        return self._dict.get('tracking_url')

    @property
    def tracking_urls(self):
        return self._dict.get('tracking_urls')

    @property
    def receipt(self):
        return Receipt(self._dict.get('receipt'))

    @property
    def line_items(self):
        return [LineItem(x) for x in self._dict.get('line_items', [])]
