from ...base import BaseParser, string_to_float


class Location(BaseParser):
    """
    Parser for basic location information such as city, state, and zip.
    """

    @property
    def country_code(self):
        """
        The two-letter code (ISO 3166-1 alpha-2 two-letter country code) for the country of the address.
        :return:
        """
        return self._dict.get('country_code')

    @property
    def province_code(self):
        """
        The two-letter abbreviation of the state or province of the address.
        :return:
        """
        return self._dict.get('province_code')

    @property
    def name(self):
        """
        The full name of the person associated with the address.
        :return:
        """
        return self._dict.get('name')

    @property
    def address_1(self):
        """
        Street address.
        :return:
        """
        return self._dict.get('address1')

    @property
    def address_2(self):
        """
        Optional field for the street address.
        :return:
        """
        return self._dict.get('address2')

    @property
    def city(self):
        """
        The city of the address.
        :return:
        """
        return self._dict.get('city')

    @property
    def zip(self):
        """
        The zip/postal-code of the address.
        :return:
        """
        return self._dict.get('zip')


class Address(Location):
    """
    Parser which contains more descriptive information about a location/address such as name and phone number.
    """

    # Address has no id field

    @property
    def first_name(self):
        """
        The first name of the person associated with the address.
        :return:
        """
        return self._dict.get('first_name')

    @property
    def phone(self):
        """
        The phone number of the address.
        :return:
        """
        return self._dict.get('phone')

    @property
    def province(self):
        """
        The name of the state or province of the address.
        :return:
        """
        return self._dict.get('province')

    @property
    def country(self):
        """
        The name of the country of the address.
        :return:
        """
        return self._dict.get('country')

    @property
    def last_name(self):
        """
        The last name of the person associated with the address.
        :return:
        """
        return self._dict.get('last_name')

    @property
    def company(self):
        """
        The company of the person associated with the address.
        :return:
        """
        return self._dict.get('company')

    @property
    def longitude(self):
        """
        The longitude of the address.
        :return:
        """
        return self._dict.get('longitude')

    @property
    def latitude(self):
        """
        The latitude of the address.
        :return:
        """
        return self._dict.get('latitude')

    @property
    def default(self):
        """
        Boolean value whether or not the address is to be used as the default address.
        :return:
        """
        return self._dict.get('default')
