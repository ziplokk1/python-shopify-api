import datetime

from dateutil import parser as date_parser


class Base(object):

    def __init__(self, d=None, **kwargs):
        self._dict = d or kwargs or {}  # Prevent exceptions when getting data from d when d is None

    @property
    def id(self):
        return self._dict.get('id')

    @staticmethod
    def convert_timestamp(dt_str):
        """
        Convert a formatted timestamp to a datetime object.

        :param dt_str: Timestamp string (2016-01-01T11:00:00-5:00)
        :return: datetime object from timestamp.
        """
        if dt_str:
            return date_parser.parse(dt_str)
        return None

    @staticmethod
    def convert_datetime(dt):
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

    @property
    def __dict__(self):
        return self._dict

    def __str__(self):
        return str(self._dict)
