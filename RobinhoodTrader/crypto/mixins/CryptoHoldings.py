from __future__ import absolute_import

from ...RobinhoodSession import RobinhoodSession
from ...wrappers import auth_required
from ...endpoints import nummus

from .Cryptocurrencies import Cryptocurrencies


class CryptoHoldings(Cryptocurrencies):
    session: RobinhoodSession

    @auth_required
    def get_crypto_holdings(self):
        endpoint = nummus.holdings()
        return self.session.get_data(endpoint, timeout=15)
