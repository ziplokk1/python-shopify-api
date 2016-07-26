from ...base import BaseParser, string_to_float


class TaxLine(BaseParser):
    """
    Parser for objects in the tax_lines list object.
    """

    @property
    def title(self):
        return self._dict.get('title')

    @title.setter
    def title(self, val):
        self._dict['title'] = val

    @property
    def price(self):
        return string_to_float(self._dict.get('price'))

    @price.setter
    def price(self, val):
        self._dict['price'] = str(val)

    @property
    def rate(self):
        return self._dict.get('rate')

    @rate.setter
    def rate(self, val):
        self._dict['rate'] = float(val)
