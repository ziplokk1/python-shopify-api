from .address import Location
from .tax_line import TaxLine
from .note_attribute import NoteAttribute
from ...base import BaseParser, string_to_float


class LineItem(BaseParser):
    """
    Parser for an item in an order.
    """

    @property
    def variant_id(self):
        """
        The id of the product variant being fulfilled.
        :return:
        """
        return self._dict.get('variant_id')

    @property
    def title(self):
        """
        The title of the product.
        :return:
        """
        return self._dict.get('title')

    @property
    def quantity(self):
        """
        The number of items in the fulfillment.
        :return:
        """
        return self._dict.get('quantity')

    @property
    def price(self):
        """
        The price of the item.
        :return:
        """
        return string_to_float(self._dict.get('price'))

    @property
    def grams(self):
        """
        The weight of the item in grams.
        :return:
        """
        return self._dict.get('grams')

    @property
    def sku(self):
        """
        A unique identifier of the item in the fulfillment.
        :return:
        """
        return self._dict.get('sku')

    @property
    def variant_title(self):
        """
        The title of the product variant being fulfilled.
        :return:
        """
        return self._dict.get('variant_title')

    @property
    def vendor(self):
        """
        The name of the supplier of the item.
        :return:
        """
        return self._dict.get('vendor')

    @property
    def fulfillment_service(self):
        """
        Service provider who is doing the fulfillment.
        :return:
        """
        return self._dict.get('fulfillment_service')

    @property
    def product_id(self):
        """
        The unique numeric identifier for the product in the fulfillment.
        :return:
        """
        return self._dict.get('product_id')

    @property
    def requires_shipping(self):
        """
        Specifies whether or not a customer needs to provide a shipping address when placing an order for this product variant.

        Valid values are: True or False
        :return:
        """
        return self._dict.get('requires_shipping')

    @property
    def taxable(self):
        # ToDo: Find documentation
        return self._dict.get('taxable')

    @property
    def gift_card(self):
        # ToDo: Find documentation
        return self._dict.get('gift_card')

    @property
    def name(self):
        # ToDo: Find documentation
        return self._dict.get('name')

    @property
    def variant_inventory_management(self):
        """
        Returns the name of the inventory management system.
        :return:
        """
        return self._dict.get('variant_inventory_management')

    @property
    def properties(self):
        """
        Returns additional properties associated with the line item.
        :return:
        """
        # NoteAttribute instance is used since it contains the same data as
        # the properties element.
        return [NoteAttribute(x) for x in self._dict.get('properties', [])]

    @property
    def product_exists(self):
        """
        States whether or not the product exists. Valid values are True or False.
        :return:
        """
        return self._dict.get('product_exists')

    @property
    def fulfillable_quantity(self):
        """
        The amount available to fulfill.

        This is the quantity - max(refunded_quantity, fulfilled_quantity) - pending_fulfilled_quantity - open_fulfilled_quantity.
        :return:
        """
        return self._dict.get('fulfillable_quantity')

    @property
    def total_discount(self):
        # ToDo: Find documentation
        return string_to_float(self._dict.get('total_discount'))

    @property
    def fulfillment_status(self):
        """
        Status of an order in terms of the line_items being fulfilled.

        Values:
            - fulfilled
            - None
            - partial
        :return:
        """
        return self._dict.get('fulfillment_status')

    @property
    def tax_lines(self):
        # ToDo: Find documentation
        return [TaxLine(x) for x in self._dict.get('tax_lines', [])]

    @property
    def origin_location(self):
        # ToDo: Find documentation
        return Location(self._dict.get('origin_location'))

    @property
    def destination_location(self):
        # ToDo: Find documentation
        return Location(self._dict.get('destination_location'))
