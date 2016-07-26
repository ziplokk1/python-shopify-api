from ...base import BaseParser


class PaymentDetail(BaseParser):

    @property
    def credit_card_bin(self):
        return self._dict.get('credit_card_bin')

    @property
    def avs_result_code(self):
        return self._dict.get('avs_result_code')

    @property
    def cvv_result_code(self):
        return self._dict.get('cvv_result_code')

    @property
    def credit_card_number(self):
        return self._dict.get('credit_card_number')

    @property
    def credit_card_company(self):
        return self._dict.get('credit_card_company')
