from __future__ import absolute_import

from .RobinhoodSession import RobinhoodSession
from .stocks import StockTrader
from .crypto import CryptoTrader

import pprint


class RobinhoodTrader(StockTrader, CryptoTrader):
    def __init__(self):
        self.session = RobinhoodSession()

    def login(self, credentials=(None, None)):
        self.session.login(credentials)

    def logout(self):
        self.session.logout()

    def print_data(self, data):
        pprint.pprint(data, indent=4)
