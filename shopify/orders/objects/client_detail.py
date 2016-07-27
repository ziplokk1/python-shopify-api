from ...base import BaseParser


class ClientDetail(BaseParser):
    """
    An object containing information about the client machine such as the browser IP and user agent.
    """

    @property
    def browser_ip(self):
        """
        The browser IP address.
        :return:
        """
        return self._dict.get('browser_ip')

    @property
    def accept_language(self):
        """
        Accept-Language header value.
        :return:
        """
        return self._dict.get('accept_language')

    @property
    def user_agent(self):
        """
        User agent string from the User-Agent header.
        :return:
        """
        return self._dict.get('user_agent')

    @property
    def session_hash(self):
        """
        A hash of the session.
        :return:
        """
        return self._dict.get('session_hash')

    @property
    def browser_width(self):
        """
        The browser screen width in pixels, if available.
        :return:
        """
        return self._dict.get('browser_width')

    @property
    def browser_height(self):
        """
        The browser screen height in pixels, if available.
        :return:
        """
        return self._dict.get('browser_height')
