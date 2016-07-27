from ...base import BaseParser, string_to_datetime
from ...orders.objects.line_item import LineItem


class Receipt(BaseParser):
    """
    Text field that provides information about the receipt.
    """

    @property
    def testcase(self):
        """
        States whether or not the fulfillment was a testcase.

        Valid values are True or False.
        :return:
        """
        return self._dict.get('testcase')

    @property
    def authorization(self):
        """
        The authorization code.
        :return:
        """
        return self._dict.get('authorization')


class Fulfillment(BaseParser):

    @property
    def order_id(self):
        """
        The unique numeric identifier for the order.
        :return:
        """
        return self._dict.get('order_id')

    @property
    def status(self):
        """
        The status of the fulfillment.

        Valid values are:
            - pending (The fulfillment is pending).
            - open (The fulfillment has been acknowledged by the service and is in processing).
            - success (The fulfillment was successful).
            - cancelled (The fulfillment was cancelled).
            - error (There was an error with the fulfillment request).
            - failure (The fulfillment request failed).
        :return:
        """
        return self._dict.get('status')

    @property
    def created_at(self):
        """
        The date and time when the fulfillment was created.
        :return:
        """
        return string_to_datetime(self._dict.get('created_at'))

    @property
    def service(self):
        # ToDo: Find documentation
        return self._dict.get('service')

    @property
    def updated_at(self):
        """
        The date and time when the fulfillment was last modified.
        :return:
        """
        return string_to_datetime(self._dict.get('updated_at'))

    @property
    def tracking_company(self):
        """
        The name of the shipping company.
        :return:
        """
        return self._dict.get('tracking_company')

    @property
    def shipment_status(self):
        # ToDo: Find documentation
        return self._dict.get('shipment_status')

    @property
    def tracking_number(self):
        # ToDo: Find documentation
        return self._dict.get('tracking_number')

    @property
    def tracking_numbers(self):
        """
        A list of shipping numbers, provided by the shipping company.
        :return:
        """
        return self._dict.get('tracking_numbers', [])

    @property
    def tracking_url(self):
        # ToDo: Find documentation
        return self._dict.get('tracking_url')

    @property
    def tracking_urls(self):
        """
        The URLs to track the fulfillment.
        :return:
        """
        return self._dict.get('tracking_urls', [])

    @property
    def receipt(self):
        """
        Text field that provides information about the receipt.
        :return:
        """
        return Receipt(self._dict.get('receipt'))

    @property
    def line_items(self):
        """
        A historical record of each item in the fulfillment.
        :return:
        """
        return [LineItem(x) for x in self._dict.get('line_items', [])]
