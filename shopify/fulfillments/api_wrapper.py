import requests
import json

from ..base import ShopifyApiWrapper, datetime_to_string, ShopifyApiError


class FulfillmentsApiWrapper(ShopifyApiWrapper):

    max_results_limit = 250

    list_endpoint = '/admin/orders/{}/fulfillments.json'

    def list(self, id_, limit=50, page=1, since_id=None, created_at_min=None, created_at_max=None, updated_at_min=None, updated_at_max=None, fields=()):
        """
        Return a list of fulfillments.

        :param id_: The ID element's value from an order.
        :param limit: Amount of results. (default 50).
        :param page: Page to show. (default 1).
        :param since_id: Restrict results to after the specified ID.
        :param created_at_min: Show fulfillments created after date.
        :param created_at_max: Show fulfillments created before date.
        :param updated_at_min: Show fulfillments last updated after date.
        :param updated_at_max: Show fulfillments last updated before date.
        :param fields: List of fields to include in the response.
        :return:
        """
        if limit > self.max_results_limit:
            raise ValueError('`limit` cannot exceed {}'.format(self.max_results_limit))
        params = dict(
            limit=limit,
            page=page,
            since_id=since_id,
            created_at_min=datetime_to_string(created_at_min),
            created_at_max=datetime_to_string(created_at_max),
            updated_at_min=datetime_to_string(updated_at_min),
            updated_at_max=datetime_to_string(updated_at_max),
            fields=','.join(fields)
        )
        params = self.remove_empty(params)

        endpoint = self.list_endpoint.format(id_)
        url = self.url_host() + endpoint
        response = requests.get(url, params=params)

        err = ShopifyApiError(response)
        if err.has_error():
            raise err

        with open('fulfillments-list.json', 'wb') as f:
            f.write(response.content)

        response.raise_for_status()

        data = json.loads(response.content)

        return data
