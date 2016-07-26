from .address import Location
from .tax_line import TaxLine
from ...base import BaseParser, string_to_float


class LineItem(BaseParser):

    @property
    def variant_id(self):
        return self._dict.get('variant_id')

    @property
    def title(self):
        return self._dict.get('title')

    @property
    def quantity(self):
        return self._dict.get('quantity')

    @property
    def price(self):
        return string_to_float(self._dict.get('price'))

    @property
    def grams(self):
        return self._dict.get('grams')

    @property
    def sku(self):
        return self._dict.get('sku')

    @property
    def variant_title(self):
        return self._dict.get('variant_title')

    @property
    def vendor(self):
        return self._dict.get('vendor')

    @property
    def fulfillment_service(self):
        return self._dict.get('fulfillment_service')

    @property
    def product_id(self):
        return self._dict.get('product_id')

    @property
    def requires_shipping(self):
        return self._dict.get('requires_shipping')

    @property
    def taxable(self):
        return self._dict.get('taxable')

    @property
    def gift_card(self):
        return self._dict.get('gift_card')

    @property
    def name(self):
        return self._dict.get('name')

    @property
    def variant_inventory_management(self):
        return self._dict.get('variant_inventory_management')

    @property
    def properties(self):
        # ToDo: See what the properties list contains in response.
        return self._dict.get('properties', [])

    @property
    def product_exists(self):
        return self._dict.get('product_exists')

    @property
    def fulfillable_quantity(self):
        return self._dict.get('fulfillable_quantity')

    @property
    def total_discount(self):
        return string_to_float(self._dict.get('total_discount'))

    @property
    def fulfillment_status(self):
        return self._dict.get('fulfillment_status')

    @property
    def tax_lines(self):
        return [TaxLine(x) for x in self._dict.get('tax_lines', [])]

    @property
    def origin_location(self):
        return Location(self._dict.get('origin_location'))

    @property
    def destination_location(self):
        return Location(self._dict.get('destination_location'))
