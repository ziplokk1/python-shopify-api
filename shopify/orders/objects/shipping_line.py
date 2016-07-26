from ...base import BaseParser, string_to_float
from .tax_line import TaxLine


class ShippingLine(BaseParser):

    @property
    def title(self):
        return self._dict.get('title')

    @property
    def price(self):
        return string_to_float(self._dict.get('price'))

    @property
    def code(self):
        return self._dict.get('code')

    @property
    def source(self):
        return self._dict.get('source')

    @property
    def phone(self):
        return self._dict.get('phone')

    @property
    def requested_fulfillment_service_id(self):
        return self._dict.get('requested_fulfillment_service_id')

    @property
    def delivery_category(self):
        return self._dict.get('delivery_category')

    @property
    def carrier_identifier(self):
        return self._dict.get('carrier_identifier')

    @property
    def tax_lines(self):
        return [TaxLine(x) for x in self._dict.get('tax_lines', [])]
