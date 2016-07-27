from ...base import BaseParser, string_to_datetime, string_to_float


class Transaction(BaseParser):

    @property
    def order_id(self):
        return self._dict.get('order_id')

    @property
    def amount(self):
        return string_to_float(self._dict.get('amount'))

    @property
    def kind(self):
        return self._dict.get('kind')

    @property
    def gateway(self):
        return self._dict.get('gateway')

    @property
    def status(self):
        return self._dict.get('status')

    @property
    def message(self):
        return self._dict.get('message')

    @property
    def created_at(self):
        return string_to_datetime(self._dict.get('created_at'))

    @property
    def test(self):
        return self._dict.get('test')

    @property
    def authorization(self):
        return self._dict.get('authorization')

    @property
    def currency(self):
        return self._dict.get('currency')

    @property
    def location_id(self):
        return self._dict.get('location_id')

    @property
    def user_id(self):
        return self._dict.get('user_id')

    @property
    def parent_id(self):
        return self._dict.get('parent_id')

    @property
    def device_id(self):
        return self._dict.get('device_id')

    @property
    def receipt(self):
        # ToDo: Figure out what elements are in receipt
        return self._dict.get('receipt')

    @property
    def error_code(self):
        return self._dict.get('error_code')

    @property
    def source_name(self):
        return self._dict.get('source_name')
