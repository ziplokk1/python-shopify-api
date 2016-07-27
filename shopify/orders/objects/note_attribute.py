from ...base import BaseParser


class NoteAttribute(BaseParser):

    @property
    def name(self):
        return self._dict.get('name')

    @property
    def value(self):
        return self._dict.get('value')
