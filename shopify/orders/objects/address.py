from ...base import BaseParser, string_to_float


class Location(BaseParser):
    """
    Used to parse out origin_location and destination_location objects contained in a line_item object.
    """

    @property
    def country_code(self):
        return self._dict.get('country_code')

    @property
    def province_code(self):
        return self._dict.get('province_code')

    @property
    def name(self):
        return self._dict.get('name')

    @property
    def address_1(self):
        return self._dict.get('address1')

    @property
    def address_2(self):
        return self._dict.get('address2')

    @property
    def city(self):
        return self._dict.get('city')

    @property
    def zip(self):
        return self._dict.get('zip')


class Address(Location):
    """
    Used to parse out billing_address and shipping_address objects.
    """

    # Address has no id field

    @property
    def first_name(self):
        return self._dict.get('first_name')

    @property
    def phone(self):
        return self._dict.get('phone')

    @property
    def province(self):
        return self._dict.get('province')

    @property
    def country(self):
        return self._dict.get('country')

    @property
    def last_name(self):
        return self._dict.get('last_name')

    @property
    def company(self):
        return self._dict.get('company')

    @property
    def longitude(self):
        return self._dict.get('longitude')

    @property
    def latitude(self):
        return self._dict.get('latitude')

    @property
    def default(self):
        return self._dict.get('default')