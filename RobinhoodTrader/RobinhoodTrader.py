from __future__ import absolute_import

from .RobinhoodSession import RobinhoodSession
from .stocks import StockMixins
from .crypto import CryptoMixins

import pprint


class RobinhoodTrader(StockMixins, CryptoMixins):
    def __init__(self):
        self.session = RobinhoodSession()

    def login(self, credentials=(None, None), use_config=True):
        self.session.login(credentials, use_config)

    def logout(self):
        self.session.logout()
