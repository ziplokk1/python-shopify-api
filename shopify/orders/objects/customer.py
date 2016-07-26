from ...base import BaseParser, string_to_datetime, string_to_float
from .address import Address


class Customer(BaseParser):

    @property
    def email(self):
        return self._dict.get('email')

    @property
    def accepts_marketing(self):
        return self._dict.get('accepts_marketing')

    @property
    def created_at(self):
        return string_to_datetime(self._dict.get('created_at'))

    @property
    def updated_at(self):
        return string_to_datetime(self._dict.get('updated_at'))

    @property
    def first_name(self):
        return self._dict.get('first_name')

    @property
    def last_name(self):
        return self._dict.get('last_name')

    @property
    def orders_count(self):
        return self._dict.get('orders_count')

    @property
    def state(self):
        return self._dict.get('state')

    @property
    def total_spent(self):
        return string_to_float(self._dict.get('total_spent'))

    @property
    def last_order_id(self):
        return self._dict.get('last_order_id')

    @property
    def note(self):
        return self._dict.get('note')

    @property
    def verified_email(self):
        return self._dict.get('verified_email')

    @property
    def multipass_identifier(self):
        return self._dict.get('multipass_identifier')

    @property
    def tax_exempt(self):
        return self._dict.get('tax_exempt')

    @property
    def tags(self):
        # ToDo: return tuple of individual tags.
        return self._dict.get('tags')

    @property
    def last_order_name(self):
        return self._dict.get('last_order_name')

    @property
    def default_address(self):
        return Address(self._dict.get('default_address'))
