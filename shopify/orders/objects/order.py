from ...base import BaseParser, string_to_datetime, string_to_float
from .address import Address
from .line_item import LineItem
from .tax_line import TaxLine
from .shipping_line import ShippingLine
from .client_detail import ClientDetail
from .payment_detail import PaymentDetail
from .customer import Customer


class Order(BaseParser):

    @property
    def email(self):
        return self._dict.get('email')

    @property
    def closed_at(self):
        return string_to_datetime(self._dict.get('closed_at'))

    @property
    def created_at(self):
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
        return self._dict.get('currency')

    @property
    def financial_status(self):
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
        return self._dict.get('cart_token')

    @property
    def buyer_accepts_marketing(self):
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
        return string_to_datetime(self._dict.get('cancelled_at'))

    @property
    def cancel_reason(self):
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
        return self._dict.get('browser_ip')

    @property
    def landing_site_ref(self):
        return self._dict.get('landing_site_ref')

    @property
    def order_number(self):
        return self._dict.get('order_number')

    @property
    def discount_codes(self):
        # ToDo: Figure out what discount_codes element contains.
        return self._dict.get('discount_codes', [])

    @property
    def note_attributes(self):
        # ToDo: Figure out what note_attributes element contains.
        return self._dict.get('note_attributes', [])

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
        return self._dict.get('fulfillment_status')

    @property
    def tax_lines(self):
        return [TaxLine(x) for x in self._dict.get('tax_lines', [])]

    @property
    def tags(self):
        # ToDo: return tuple containing individual tags.
        return self._dict.get('tags')

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
        return Address(self._dict.get('shipping_address'))

    @property
    def fulfillments(self):
        # ToDo: Figure out what fulfillments returns
        return []

    @property
    def client_details(self):
        return ClientDetail(self._dict.get('client_details'))

    @property
    def refunds(self):
        # ToDo: Figure out what refunds returns
        return []

    @property
    def payment_details(self):
        return PaymentDetail(self._dict.get('payment_details'))

    @property
    def customer(self):
        return Customer(self._dict.get('customer'))
