import json


class ShopifyApiError(Exception):
    """
    Used to check if a response is an error and parse out the error.
    """

    def __init__(self, response):
        self.response = response
        content = self.response.content
        if content:
            self.content = json.loads(self.response.content)
        else:
            self.content = {}
        Exception.__init__(self, self.message)

    def has_error(self):
        return bool(self.content.get('errors'))

    @property
    def message(self):
        errors = self.content.get('errors', {})
        msg = ''
        if isinstance(errors, dict):
            for category, message in errors.items():
                # Error Category, Message
                msg += '({} - {})'.format(category, message)
        else:
            msg += errors
        return msg


class ShopifyApiWrapper(object):

    def __init__(self, api_key, password, store_name):
        self.api_key = api_key
        self.password = password
        self.store_name = store_name

    @staticmethod
    def remove_empty(d):
        """
        Return a new dictionary object from the old one without any items with falsey values.
        :param d:
        :return:
        """
        return {k: v for k, v in d.items() if v}

    def url_host(self):
        """
        Format the URL host with the api_key, password, and store name for access to shopify's api.
        :return: Formatted URL (https://api_key:password@store_name.myshopify.com)
        """
        return 'https://{}:{}@{}.myshopify.com'.format(self.api_key, self.password, self.store_name)
