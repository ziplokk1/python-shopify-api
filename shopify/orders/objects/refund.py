from ...base import BaseParser, string_to_datetime
from .transaction import Transaction
from .line_item import LineItem


class Refund(BaseParser):

    @property
    def order_id(self):
        return self._dict.get('order_id')

    @property
    def created_at(self):
        return string_to_datetime(self._dict.get('created_at'))

    @property
    def note(self):
        return self._dict.get('note')

    @property
    def restock(self):
        return self._dict.get('restock')

    @property
    def user_id(self):
        return self._dict.get('user_id')

    @property
    def refund_line_items(self):
        return [LineItem(x) for x in self._dict.get('refund_line_items', [])]

    @property
    def transactions(self):
        return [Transaction(x) for x in self._dict.get('transactions', [])]

    @property
    def order_adjustments(self):
        # ToDo: Figure out what order_adjustments returns
        return [x for x in self._dict.get('order_adjustments', [])]
