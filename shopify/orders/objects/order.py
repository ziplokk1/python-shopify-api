from ...base import BaseParser, string_to_datetime, string_to_float
from .address import Address
from .line_item import LineItem
from .tax_line import TaxLine
from .shipping_line import ShippingLine
from .client_detail import ClientDetail
from .payment_detail import PaymentDetail
from .customer import Customer
from .discount_code import DiscountCode
from .note_attribute import NoteAttribute
from ...fulfillments import Fulfillment
from .refund import Refund


class Order(BaseParser):

    @property
    def email(self):
        """
        The customer's email address.

        Is required when a billing address is present.
        :return:
        """
        return self._dict.get('email')

    @property
    def closed_at(self):
        """
        The date and time when the order was closed.

        If the order was not closed, this value is None.
        :return:
        """
        return string_to_datetime(self._dict.get('closed_at'))

    @property
    def created_at(self):
        """
        By default, this auto-generated property is the date and time when the order was created in Shopify.

        If you are importing orders to the Shopify platform from another system,
            the writable processed_at property will override the created_at date.
        :return:
        """
        return string_to_datetime(self._dict.get('created_at'))

    @property
    def updated_at(self):
        return string_to_datetime(self._dict.get('updated_at'))

    @property
    def number(self):
        return self._dict.get('number')

    @property
    def note(self):
        return self._dict.get('note')

    @property
    def token(self):
        return self._dict.get('token')

    @property
    def gateway(self):
        return self._dict.get('gateway')

    @property
    def test(self):
        return self._dict.get('test')

    @property
    def total_price(self):
        return string_to_float(self._dict.get('total_price'))

    @property
    def subtotal_price(self):
        return string_to_float(self._dict.get('subtotal_price'))

    @property
    def total_weight(self):
        return self._dict.get('total_weight')

    @property
    def total_tax(self):
        return string_to_float(self._dict.get('total_tax'))

    @property
    def taxes_included(self):
        return self._dict.get('taxes_included')

    @property
    def currency(self):
        """
        The three letter code (ISO 4217) for the currency used for the payment.
        :return:
        """
        return self._dict.get('currency')

    @property
    def financial_status(self):
        """
        The financial processing status for the order.

        Values can be one of:
            - pending
            - authorized
            - partially_paid
            - paid (default)
            - partially_refunded
            - refunded
            - voided
        :return:
        """
        return self._dict.get('financial_status')

    @property
    def confirmed(self):
        return self._dict.get('confirmed')

    @property
    def total_discounts(self):
        return string_to_float(self._dict.get('total_discounts'))

    @property
    def total_line_items_price(self):
        return string_to_float(self._dict.get('total_line_items_price'))

    @property
    def cart_token(self):
        """
        Unique identifier for a particular cart that is attached to a particular order.
        :return:
        """
        return self._dict.get('cart_token')

    @property
    def buyer_accepts_marketing(self):
        """
        Indicates whether or not the person who placed the order would like to receive email updates from the shop.

        This is set when checking the "I want to receive occasional emails about new products,
            promotions and other news" checkbox during checkout.
        Valid values are True and False.
        :return:
        """
        return self._dict.get('buyer_accepts_marketing')

    @property
    def name(self):
        return self._dict.get('name')

    @property
    def referring_site(self):
        return self._dict.get('referring_site')

    @property
    def landing_site(self):
        return self._dict.get('landing_site')

    @property
    def cancelled_at(self):
        """
        The date and time when the order was cancelled.

        If the order was not cancelled, this value is None.
        :return:
        """
        return string_to_datetime(self._dict.get('cancelled_at'))

    @property
    def cancel_reason(self):
        """
        The reason why the order was cancelled.

        If the order was not cancelled, this value is None.
        If the order was cancelled, the value will be one of the following:
            - customer: The customer changed or cancelled the order.
            - fraud: The order was fraudulent.
            - inventory: Items in the order were not in inventory.
            - other: The order was cancelled for a reason not in the list above.
        :return:
        """
        return self._dict.get('cancel_reason')

    @property
    def total_price_usd(self):
        return string_to_float(self._dict.get('total_price_usd'))

    @property
    def checkout_token(self):
        return self._dict.get('checkout_token')

    @property
    def reference(self):
        return self._dict.get('reference')

    @property
    def user_id(self):
        return self._dict.get('user_id')

    @property
    def location_id(self):
        return self._dict.get('location_id')

    @property
    def source_identifier(self):
        return self._dict.get('source_identifier')

    @property
    def source_url(self):
        return self._dict.get('source_url')

    @property
    def processed_at(self):
        return string_to_datetime(self._dict.get('processed_at'))

    @property
    def device_id(self):
        return self._dict.get('device_id')

    @property
    def browser_ip(self):
        """
        The IP address of the browser used by the customer when placing the order.
        :return:
        """
        return self._dict.get('browser_ip')

    @property
    def landing_site_ref(self):
        return self._dict.get('landing_site_ref')

    @property
    def order_number(self):
        return self._dict.get('order_number')

    @property
    def discount_codes(self):
        """
        Applicable discount codes that can be applied to the order.

        If no codes exist the value will default to an empty list.
        :return:
        """
        return [DiscountCode(x) for x in self._dict.get('discount_codes', [])]

    @property
    def note_attributes(self):
        return [NoteAttribute(x) for x in self._dict.get('note_attributes', [])]

    @property
    def payment_gateway_names(self):
        return self._dict.get('payment_gateway_names', [])

    @property
    def processing_method(self):
        return self._dict.get('processing_method')

    @property
    def checkout_id(self):
        return self._dict.get('checkout_id')

    @property
    def source_name(self):
        return self._dict.get('source_name')

    @property
    def fulfillment_status(self):
        """
        Show fulfillment status.

        Values:
            - fulfilled (Every line item in the order has been fulfilled)
            - null (None of the line items in the order have been fulfilled)
            - partial (At least one line item in the order has been fulfilled)
        :return:
        """
        return self._dict.get('fulfillment_status')

    @fulfillment_status.setter
    def fulfillment_status(self, val):
        self._dict['fulfillment_status'] = val

    @property
    def tax_lines(self):
        return [TaxLine(x) for x in self._dict.get('tax_lines', [])]

    @property
    def tags(self):
        """
        Tags are additional short descriptors, commonly used for filtering and searching.
        :return:
        """
        return tuple([x.strip() for x in self._dict.get('tags').split(',')])

    @property
    def contact_email(self):
        return self._dict.get('contact_email')

    @property
    def order_status_url(self):
        return self._dict.get('order_status_url')

    @property
    def line_items(self):
        return [LineItem(x) for x in self._dict.get('line_items', [])]

    @property
    def shipping_lines(self):
        return [ShippingLine(x) for x in self._dict.get('shipping_lines', [])]

    @property
    def billing_address(self):
        return Address(self._dict.get('billing_address'))

    @property
    def shipping_address(self):
        """
        The mailing address associated with the payment method.

        This address is an optional field that will not be available on orders that do not require one.
        :return:
        """
        return Address(self._dict.get('shipping_address'))

    @property
    def fulfillments(self):
        """
        Return a list of Fulfillment objects parsed from the fulfillments element of the order.
        :return:
        """
        return [Fulfillment(x) for x in self._dict.get('fulfillments', [])]

    @property
    def client_details(self):
        """
        An object containing information about the client.
        return:
        """
        return ClientDetail(self._dict.get('client_details'))

    @property
    def refunds(self):
        return [Refund(x) for x in self._dict.get('refunds', [])]

    @property
    def payment_details(self):
        return PaymentDetail(self._dict.get('payment_details'))

    @property
    def customer(self):
        """
        An object containing information about the customer.

        It is important to note that the order may not have a customer and consumers
            should not depend on the existence of a customer object.
        This value may be falsey if the order was created through Shopify POS.
        :return:
        """
        return Customer(self._dict.get('customer'))
