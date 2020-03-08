from __future__ import absolute_import

from .session import RobinhoodSession
from .stocks import StockMixins
from .crypto import CryptoMixins

import pprint


class RobinhoodTrader(StockMixins, CryptoMixins):
    def __init__(self, credentials=(None, None), qr_code=None):
        self.session = RobinhoodSession(credentials, qr_code)

    def login(self, credentials=(None, None), qr_code=None, use_config=True):
        self.session.login(credentials, qr_code, use_config)

    def logout(self):
        self.session.logout()
