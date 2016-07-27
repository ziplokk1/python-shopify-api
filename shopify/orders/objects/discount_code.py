from ...base import BaseParser, string_to_float


class DiscountCode(BaseParser):
    """
    Parser for any applicable discounts to an order.
    """

    @property
    def code(self):
        """
        The discount code.
        :return:
        """
        return self._dict.get('code')

    @property
    def amount(self):
        """
        The amount of the discount.
        :return:
        """
        return string_to_float(self._dict.get('amount'))

    @property
    def type(self):
        """
        The type of discount.

        Can be one of:
            - percentage
            - shipping
            - fixed_amount (default)
        :return:
        """
        return self._dict.get('type')
