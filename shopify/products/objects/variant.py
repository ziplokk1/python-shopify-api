from ...base import BaseParser, datetime_to_string, string_to_datetime


class Variant(BaseParser):

    @property
    def product_id(self):
        return self._dict.get('product_id')

    # No product_id setter since that value shouldn't be modified.

    @property
    def title(self):
        return self._dict.get('title')

    @title.setter
    def title(self, val):
        self._dict['title'] = val

    @property
    def price(self):
        prc = self._dict.get('price')
        if prc:
            return float(prc)
        return None

    @price.setter
    def price(self, val):
        self._dict['price'] = str(val)

    @property
    def sku(self):
        return self._dict.get('sku')

    @sku.setter
    def sku(self, val):
        self._dict['sku'] = val

    @property
    def position(self):
        return self._dict.get('position')

    @position.setter
    def position(self, val):
        self._dict['position'] = int(val)

    @property
    def grams(self):
        return self._dict.get('grams')

    @grams.setter
    def grams(self, val):
        self._dict['grams'] = int(val)

    @property
    def inventory_policy(self):
        return self._dict.get('inventory_policy')

    @inventory_policy.setter
    def inventory_policy(self, val):
        self._dict['inventory_policy'] = val

    @property
    def compare_at_price(self):
        return self._dict.get('compare_at_price')

    @compare_at_price.setter
    def compare_at_price(self, val):
        self._dict['compare_at_price'] = val

    @property
    def fulfillment_service(self):
        return self._dict.get('fulfillment_service')

    @fulfillment_service.setter
    def fulfillment_service(self, val):
        self._dict['fulfillment_service'] = val

    @property
    def inventory_management(self):
        return self._dict.get('inventory_management')

    @inventory_management.setter
    def inventory_management(self, val):
        self._dict['inventory_management'] = val

    @property
    def option1(self):
        return self._dict.get('option1')

    @option1.setter
    def option1(self, val):
        self._dict['option1'] = val

    @property
    def option2(self):
        return self._dict.get('option2')

    @option2.setter
    def option2(self, val):
        self._dict['option2'] = val

    @property
    def option3(self):
        return self._dict.get('option3')

    @option3.setter
    def option3(self, val):
        self._dict['option3'] = val

    @property
    def created_at(self):
        return string_to_datetime(self._dict.get('created_at'))

    @created_at.setter
    def created_at(self, val):
        self._dict['created_at'] = datetime_to_string(val)

    @property
    def updated_at(self):
        return string_to_datetime(self._dict.get('updated_at'))

    @updated_at.setter
    def updated_at(self, val):
        self._dict['updated_at'] = datetime_to_string(val)

    @property
    def taxable(self):
        return self._dict.get('taxable')

    @taxable.setter
    def taxable(self, val):
        self._dict['taxable'] = val

    @property
    def barcode(self):
        return self._dict.get('barcode')

    @barcode.setter
    def barcode(self, val):
        self._dict['barcode'] = val

    @property
    def image_id(self):
        return self._dict.get('image_id')

    @image_id.setter
    def image_id(self, val):
        self._dict['image_id'] = val

    @property
    def inventory_quantity(self):
        return self._dict.get('inventory_quantity')

    @inventory_quantity.setter
    def inventory_quantity(self, val):
        self._dict['inventory_quantity'] = int(val)

    @property
    def weight(self):
        return self._dict.get('weight')

    @weight.setter
    def weight(self, val):
        self._dict['weight'] = float(val) if val else None

    @property
    def weight_unit(self):
        return self._dict.get('weight_unit')

    @weight_unit.setter
    def weight_unit(self, val):
        self._dict['weight_unit'] = val

    @property
    def old_inventory_quantity(self):
        return self._dict.get('old_inventory_quantity')

    @old_inventory_quantity.setter
    def old_inventory_quantity(self, val):
        self._dict['old_inventory_quantity'] = int(val)

    @property
    def requires_shipping(self):
        return self._dict.get('requires_shipping')

    @requires_shipping.setter
    def requires_shipping(self, val):
        self._dict['requires_shipping'] = val

    def __repr__(self):
        return '<Variant id={} product_id={} title={} price={}>'.format(
            self.id, self.product_id, self.title, self.price
        )
