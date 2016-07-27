from ...base import BaseParser, string_to_datetime, string_to_float
from .address import Address


class Customer(BaseParser):
    """
    Parser which contains descriptive information about the customer such as name and email.
    """

    @property
    def email(self):
        """
        The customer's email address.
        :return:
        """
        return self._dict.get('email')

    @property
    def accepts_marketing(self):
        """
        Indicates whether or not the customer would like to receive email updates from the shop.

        Valid values are True and False.
        :return:
        """
        return self._dict.get('accepts_marketing')

    @property
    def created_at(self):
        """
        The date and time when the customer record was created.
        :return:
        """
        return string_to_datetime(self._dict.get('created_at'))

    @property
    def updated_at(self):
        """
        The date and time when the customer record was last updated.
        :return:
        """
        return string_to_datetime(self._dict.get('updated_at'))

    @property
    def first_name(self):
        """
        The customer's first name.
        :return:
        """
        return self._dict.get('first_name')

    @property
    def last_name(self):
        """
        The customer's last name.
        :return:
        """
        return self._dict.get('last_name')

    @property
    def orders_count(self):
        """
        The number of orders placed by this customer to a shop.

        Pulls the current information.
        :return:
        """
        return self._dict.get('orders_count')

    @property
    def state(self):
        """
        No documentation available.

        :return:
        """
        # ToDo: find documentation
        return self._dict.get('state')

    @property
    def total_spent(self):
        """
        No documentation available.
        :return:
        """
        # ToDo: find documentation
        return string_to_float(self._dict.get('total_spent'))

    @property
    def last_order_id(self):
        """
        No documentation available.
        :return:
        """
        # ToDo: find documentation
        return self._dict.get('last_order_id')

    @property
    def note(self):
        """
        Extra information about the customer.
        :return:
        """
        return self._dict.get('note')

    @property
    def verified_email(self):
        """
        No documentation available.
        :return:
        """
        # ToDo: find documentation
        return self._dict.get('verified_email')

    @property
    def multipass_identifier(self):
        """
        No documentation available.
        :return:
        """
        # ToDo: find documentation
        return self._dict.get('multipass_identifier')

    @property
    def tax_exempt(self):
        """
        No documentation available.
        :return:
        """
        # ToDo: find documentation
        return self._dict.get('tax_exempt')

    @property
    def tags(self):
        """
        Tags are additional short descriptors, commonly used for filtering and searching.
        :return:
        """
        return tuple([x.strip() for x in self._dict.get('tags', '').split(',')])

    @property
    def last_order_name(self):
        """
        No documentation available.
        :return:
        """
        # ToDo: find documentation
        return self._dict.get('last_order_name')

    @property
    def default_address(self):
        """
        No documentation available.
        :return:
        """
        # ToDo: find documentation
        return Address(self._dict.get('default_address'))
