from ...base import BaseParser


class Order(BaseParser):

    @property
    def email(self):
        return self._dict.get('email')

    @property
    def closed_at(self):
        return self._dict.get('closed_at')

    @property
    def created_at(self):
        return self._dict.get('created_at')

    @property
    def updated_at(self):
        return self._dict.get('updated_at')

    @property
    def number(self):
        return self._dict.get('number')

    @property
    def note(self):
        return self._dict.get('note')

    @property
    def token(self):
        return self._dict.get('token')

    @property
    def gateway(self):
        return self._dict.get('gateway')

    @property
    def test(self):
        return self._dict.get('test')
