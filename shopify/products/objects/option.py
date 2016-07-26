from ...base import BaseParser


class Option(BaseParser):

    @property
    def product_id(self):
        return self._dict.get('product_id')

    # No product_id setter since that value shouldn't be modified.

    @property
    def name(self):
        return self._dict.get('name')

    @name.setter
    def name(self, val):
        self._dict['name'] = val

    @property
    def position(self):
        return self._dict.get('position')

    @position.setter
    def position(self, val):
        self._dict['position'] = int(val)

    @property
    def values(self):
        return self._dict.get('values')

    @values.setter
    def values(self, val):
        self._dict['values'] = val

    def __repr__(self):
        return '<Option id={} product_id={} name={}>'.format(self.id, self.product_id, self.name)
