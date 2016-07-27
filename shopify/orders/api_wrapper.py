import requests
import json

from ..base import ShopifyApiWrapper, datetime_to_string, ShopifyApiError
from .objects import Order


class OrdersApiWrapper(ShopifyApiWrapper):

    max_results_limit = 250

    default_endpoint = '/admin/orders.json'
    operational_endpoint = '/admin/orders/{}.json'
    close_endpoint = '/admin/orders/{}/close.json'
    open_endpoint = '/admin/orders/{}/open.json'
    cancel_endpoint = '/admin/orders/{}/cancel.json'

    valid_status_values = [
        'open',
        'closed',
        'cancelled',
        'any'
    ]

    valid_financial_status_values = [
        'authorized',
        'pending',
        'paid',
        'partially_paid',
        'refunded',
        'voided',
        'partially_refunded',
        'any',
        'unpaid'
    ]

    valid_fulfillment_status_values = [
        'shipped',
        'partial',
        'unshipped',
        'any'
    ]

    def list(self, ids=(), limit=50, page=1, since_id=None, created_at_min=None, created_at_max=None,
             updated_at_min=None, updated_at_max=None, processed_at_min=None, processed_at_max=None, status='open',
             financial_status='any', fulfillment_status='any', fields=()):
        if limit > self.max_results_limit:
            raise ValueError('`limit` cannot exceed {}'.format(self.max_results_limit))
        if status not in self.valid_status_values:
            raise ValueError('`status` must be one of {}'.format(self.valid_status_values))
        if financial_status not in self.valid_financial_status_values:
            raise ValueError('`financial_status` must be one of {}'.format(self.valid_financial_status_values))
        if fulfillment_status not in self.valid_fulfillment_status_values:
            raise ValueError('`fulfillment_status` must be one of {}'.format(self.valid_fulfillment_status_values))
        params = dict(
            ids=','.join(ids),
            limit=limit,
            page=page,
            since_id=since_id,
            created_at_min=datetime_to_string(created_at_min),
            created_at_max=datetime_to_string(created_at_max),
            updated_at_min=datetime_to_string(updated_at_min),
            updated_at_max=datetime_to_string(updated_at_max),
            processed_at_min=datetime_to_string(processed_at_min),
            processed_at_max=datetime_to_string(processed_at_max),
            status=status,
            financial_status=financial_status,
            fulfillment_status=fulfillment_status,
            fields=','.join(fields)
        )
        params = self.remove_empty(params)
        url = self.url_host() + self.default_endpoint
        response = requests.get(url, params=params)

        with open('orders-list.json', 'wb') as f:
            f.write(response.content)

        # Check if the response was an error and raise if necessary.
        err = ShopifyApiError(response)
        if err.has_error():
            raise err

        data = json.loads(response.content)
        return [Order(x) for x in data.get('orders', [])]

    def _close(self, order_id):
        endpoint = self.close_endpoint.format(order_id)
        url = self.url_host() + endpoint

        r = requests.post(url, data='{}', headers={"Content-Type": 'application/json'})

        with open('order-close.json', 'wb') as f:
            f.write(r.content)

        err = ShopifyApiError(r)
        if err.has_error():
            raise err

        return json.loads(r.content)

    def close(self, order):
        if not order.id:
            raise ValueError('`order` object must have id.')
        return Order(self._close(order.id).get('order'))

    def close_by_id(self, id_):
        return Order(self._close(id_).get('order'))
