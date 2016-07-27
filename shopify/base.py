import json
import datetime
import urlparse

import requests
from dateutil import parser as date_parser


def datetime_to_string(dt):
    """
    Convert a datetime object to the preferred format for the shopify api. (2016-01-01T11:00:00-5:00)

    :param dt: Datetime object to convert to timestamp.
    :return: Timestamp string for the datetime object.
    """
    if not dt:
        return None
    if not isinstance(dt, datetime.datetime):
        raise ValueError('Must supply an instance of `datetime`.')
    # Calculate the utc offset of the current timezone
    # 1 is added to the total seconds to account for the time which it takes the operation to calculate
    # utcnow and local now.
    offset = int(divmod((datetime.datetime.utcnow() - datetime.datetime.now()).total_seconds() + 1, 60)[0] / 60)
    offset_str = '-%d:00' % offset
    dt_str = dt.strftime('%Y-%m-%dT%H:%M:%S')
    return dt_str + offset_str


def string_to_datetime(dt_str):
    """
    Convert a formatted timestamp to a datetime object.

    :param dt_str: Timestamp string (2016-01-01T11:00:00-5:00)
    :return: datetime object from timestamp.
    """
    if dt_str:
        return date_parser.parse(dt_str)
    return None


def string_to_float(float_str):
    """
    Convert a float in string format to a float.

    :param float_str: Float in string format ("25.01")
    :return: float from string
    """
    if float_str:
        return float(float_str)
    return None


class BaseParser(object):

    def __init__(self, d=None, **kwargs):
        self._dict = d or kwargs or {}  # Prevent exceptions when getting data from d when d is None

    @property
    def id(self):
        return self._dict.get('id')

    @property
    def __dict__(self):
        return self._dict

    def __str__(self):
        return str(self._dict)

    def __nonzero__(self):
        return bool(self._dict)


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
