import base64

from .base import Base


class Image(Base):

    def __init__(self, d, **kwargs):
        Base.__init__(self, d, **kwargs)
        self.image_location = None

    @property
    def product_id(self):
        return self._dict.get('product_id')

    # No product_id setter since that value shouldn't be modified.

    @property
    def position(self):
        return self._dict.get('position')

    @position.setter
    def position(self, val):
        self._dict['position'] = int(val)

    @property
    def created_at(self):
        return self.convert_timestamp(self._dict.get('created_at'))

    @created_at.setter
    def created_at(self, val):
        self._dict['created_at'] = self.convert_datetime(val)

    @property
    def updated_at(self):
        return self.convert_timestamp(self._dict.get('updated_at'))

    @updated_at.setter
    def updated_at(self, val):
        self._dict['updated_at'] = self.convert_datetime(val)

    @property
    def src(self):
        return self._dict.get('src')

    @src.setter
    def src(self, val):
        self._dict['src'] = val

    def attach(self, f):
        """
        Attach an image file instead of using a url.
        :param f: Path to image file.
        :return:
        """
        with open(f, 'rb') as f:
            encoded = base64.b64encode(f.read())
        self._dict['attachment'] = encoded
        self.image_location = f

    def __repr__(self):
        return '<Image id={} src={} attachment={}>'.format(self.id, self.src, self.image_location)
