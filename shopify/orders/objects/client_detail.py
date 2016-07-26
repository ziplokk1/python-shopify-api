from ...base import BaseParser


class ClientDetail(BaseParser):

    @property
    def browser_ip(self):
        return self._dict.get('browser_ip')

    @property
    def accept_language(self):
        return self._dict.get('accept_language')

    @property
    def user_agent(self):
        return self._dict.get('user_agent')

    @property
    def session_hash(self):
        return self._dict.get('session_hash')

    @property
    def browser_width(self):
        return self._dict.get('browser_width')

    @property
    def browser_height(self):
        return self._dict.get('browser_height')
