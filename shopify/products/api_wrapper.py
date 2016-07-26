import json

import requests
import datetime

from .objects import Product
from ..base import ShopifyApiWrapper, ShopifyApiError


class ProductsApiWrapper(ShopifyApiWrapper):

    valid_published_statuses = [
        'published',
        'unpublished',
        'any'
    ]

    default_endpoint = '/admin/products.json'
    operational_endpoint = '/admin/products/{}.json'

    def update(self, product):
        if not product.id:
            raise ValueError('product must have an ID to use `update`')
        endpoint = self.operational_endpoint.format(product.id)
        url = self.url_host() + endpoint
        d = json.dumps(product.__dict__)

        response = requests.put(url, data=d, headers={'Content-Type': 'application/json'})

        err_check = ShopifyApiError(response)
        if err_check.has_error():
            raise err_check

    def create(self, product):
        """
        Create a product in inventory.

        :param product: A Product object instance.
        :return:
        """
        url = self.url_host() + self.default_endpoint
        d = json.dumps(product.__dict__)
        response = requests.post(url, data=d, headers={'Content-Type': 'application/json'})

        err_check = ShopifyApiError(response)
        if err_check.has_error():
            raise err_check

        return Product(json.loads(response.content))

    def _delete(self, id_):
        """
        Delete product from inventory using the products ID.

        :param id_: The products ID to delete.
        :return:
        """
        endpoint = self.operational_endpoint.format(id_)
        url = self.url_host() + endpoint
        response = requests.delete(url)

        err_check = ShopifyApiError(response)
        if err_check.has_error():
            raise err_check

    def delete(self, product):
        """
        Delete a product from inventory.

        Use when you have a product instance returned from list().

        :param product: A Product object.
        :return:
        """
        if not product.id:
            raise ValueError('product must have an ID to use `delete`')
        self._delete(product.id)

    def delete_by_id(self, id_):
        """
        Delete a product from inventory using the product's ID.

        :param id_: The numerical id for a product.
        :return:
        """
        self._delete(id_)

    def list(self, ids=(), limit=50, page=1, since_id=None, title=None,
             vendor=None, handle=None, product_type=None, collection_id=None,
             created_at_min=None, created_at_max=None, updated_at_min=None,
             updated_at_max=None, published_at_min=None, published_at_max=None,
             published_status='any', fields=()):
        """
        Return a list of products which are associated with your shopify account.

        :param ids: product ids to request.
        :param limit: Amount of results. (maximum: 250).
        :param page: Page to show.
        :param since_id: Restrict results to after the specified ID.
        :param title: Filter by product title.
        :param vendor: Filter by product vendor.
        :param handle: Filter by product handle.
        :param product_type: Filter by product type.
        :param collection_id: Filter by collection ID.
        :param created_at_min: Show products created after date.
        :param created_at_max: Show products create before date.
        :param updated_at_min: Show products last update after date.
        :param updated_at_max: Show products last updated before date.
        :param published_at_min: Show products published after date.
        :param published_at_max: Show products published before date.
        :param published_status: Filter by published status.
            Valid Values:
                published - Show only published products.
                unpublished - Show only unpublished products.
                any - Show all products.
        :param fields: List of fields to include in the response.
        :return:
        """
        url = self.url_host() + self.default_endpoint
        if published_status not in self.valid_published_statuses:
            raise ValueError('\'{}\' is not a valid published status. Use one of {}.'.format(
                published_status, self.valid_published_statuses))
        if limit > 250:
            raise ValueError('limit must be less than 250')
        params = dict(
            ids=','.join(ids),
            limit=limit,
            page=page,
            since_id=since_id,
            title=title,
            vendor=vendor,
            handle=handle,
            product_type=product_type,
            collection_id=collection_id,
            created_at_min=self.convert_datetime(created_at_min),
            created_at_max=self.convert_datetime(created_at_max),
            updated_at_min=self.convert_datetime(updated_at_min),
            updated_at_max=self.convert_datetime(updated_at_max),
            published_at_min=self.convert_datetime(published_at_min),
            published_at_max=self.convert_datetime(published_at_max),
            published_status=published_status,
            fields=','.join(fields)
        )
        params = self.remove_empty(params)
        response = requests.get(url, params=params)
        data = json.loads(response.content)
        return [Product(x) for x in data.get('products', [])]

    @staticmethod
    def convert_datetime(dt):
        """
        Convert a datetime object to the proper format for shopify's api.
        :param dt:
        :return:
        """
        if not dt:
            return None
        if not isinstance(dt, datetime.datetime):
            raise ValueError('Must supply an instance of `datetime`.')
        # Calculate the utc offset of the current timezone
        # 1 is added to the total seconds to account for the time which it takes the operation to calculate
        # utcnow and local now.
        offset = int((datetime.datetime.utcnow() - datetime.datetime.now()).total_seconds() + 1 / 60 / 60)
        offset_str = '-%d:00' % offset
        dt_str = dt.strftime('%Y-%m-%dT%H:%M:%S')
        return dt_str + offset_str
