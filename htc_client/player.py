"""htc_client.player"""

from htc_api import Client


class Player:
    """Player object."""

    def __init__(self, username, server_code, url='http://167.99.167.17', port=51337):
        self.username = username
        self.server_code = server_code
        self.client = Client(self.username, self.server_code, url=url, port=port)
