from ...base import BaseParser, string_to_float


class DiscountCode(BaseParser):

    @property
    def code(self):
        return self._dict.get('code')

    @property
    def amount(self):
        return string_to_float(self._dict.get('amount'))

    @property
    def type(self):
        return self._dict.get('type')
