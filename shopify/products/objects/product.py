from HTMLParser import HTMLParser
import datetime

from ...base import BaseParser, datetime_to_string, string_to_datetime
from .image import Image
from .option import Option
from .variant import Variant


class Product(BaseParser):

    @property
    def title(self):
        return self._dict.get('title')

    @title.setter
    def title(self, val):
        self._dict['title'] = val

    @property
    def body_html(self):
        html = self._dict.get('body_html')
        if html:
            return HTMLParser().unescape(html)
        return None

    @body_html.setter
    def body_html(self, val):
        self._dict['body_html'] = val

    @property
    def vendor(self):
        return self._dict.get('vendor')

    @vendor.setter
    def vendor(self, val):
        self._dict['vendor'] = val

    @property
    def product_type(self):
        return self._dict.get('product_type')

    @product_type.setter
    def product_type(self, val):
        self._dict['product_type'] = val

    @property
    def created_at(self):
        return string_to_datetime(self._dict.get('created_at'))

    @created_at.setter
    def created_at(self, val):
        self._dict['created_at'] = datetime_to_string(val)

    @property
    def handle(self):
        return self._dict.get('handle')

    @handle.setter
    def handle(self, val):
        self._dict['handle'] = val

    @property
    def updated_at(self):
        return string_to_datetime(self._dict.get('updated_at'))

    @updated_at.setter
    def updated_at(self, val):
        self._dict['updated_at'] = datetime_to_string(val)

    @property
    def published_at(self):
        return string_to_datetime(self._dict.get('published_at'))

    @published_at.setter
    def published_at(self, val):
        if isinstance(val, datetime.datetime):
            val = datetime_to_string(val)
        self._dict['published_at'] = val

    @property
    def publish_on(self):
        return string_to_datetime(self._dict.get('publish_on'))

    @publish_on.setter
    def publish_on(self, val):
        if isinstance(val, datetime.datetime):
            val = datetime_to_string(val)
        self._dict['publish_on'] = val

    @property
    def published(self):
        return self._dict.get('published')

    @published.setter
    def published(self, b):
        self._dict['published'] = b

    @property
    def template_suffix(self):
        return self._dict.get('template_suffix')

    @template_suffix.setter
    def template_suffix(self, val):
        self._dict['template_suffix'] = val

    @property
    def published_scope(self):
        return self._dict.get('published_scope')

    @published_scope.setter
    def published_scope(self, val):
        self._dict['published_scope'] = val

    @property
    def tags(self):
        return self._dict.get('tags')

    @tags.setter
    def tags(self, val):
        self._dict['tags'] = val

    def add_tags(self, *args):
        t = self._dict.get('tags')
        if not t:
            self._dict['tags'] = []
        self._dict['tags'].extend(list(args))

    @property
    def image(self):
        return Image(self._dict.get('image'))

    @image.setter
    def image(self, val):
        self._dict['image'] = dict(val)

    def images(self):
        return [Image(x) for x in self._dict.get('images', [])]

    def options(self):
        return [Option(x) for x in self._dict.get('options', [])]

    def variants(self):
        return [Variant(x) for x in self._dict.get('variants', [])]

    def add_variant(self, variant):
        v = self._dict.get('variants')
        if not v:
            self._dict['variants'] = []
        self._dict['variants'].append(variant.__dict__)

    def add_option(self, option):
        o = self._dict.get('options')
        if not o:
            self._dict['options'] = []
        self._dict['options'].append(option.__dict__)

    def add_image(self, image):
        i = self._dict.get('images')
        if not i:
            self._dict['images'] = []
        self._dict['images'].append(image.__dict__)

    @property
    def __dict__(self):
        return {'product': self._dict}

    def __repr__(self):
        return '<Product id={} title={} options={} variants={} images={}>'.format(self.id, self.title, self.options(), self.variants(), self.images())
