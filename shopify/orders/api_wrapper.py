import requests

from ..base import ShopifyApiWrapper, convert_datetime


class OrdersApiWrapper(ShopifyApiWrapper):

    max_results_limit = 250

    default_endpoint = '/admin/orders.json'
    operational_endpoint = '/admin/orders/{}.json'

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
            created_at_min=convert_datetime(created_at_min),
            created_at_max=convert_datetime(created_at_max),
            updated_at_min=convert_datetime(updated_at_min),
            updated_at_max=convert_datetime(updated_at_max),
            processed_at_min=convert_datetime(processed_at_min),
            processed_at_max=convert_datetime(processed_at_max),
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
