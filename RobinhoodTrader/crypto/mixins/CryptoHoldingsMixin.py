from __future__ import absolute_import

from ...session import RobinhoodSession
from ...wrappers import auth_required
from ...endpoints import nummus
from ...datatypes import CryptoHoldings, CryptoHolding, Page

from .CryptocurrencyMixin import CryptocurrencyMixin


class CryptoHoldingsMixin(CryptocurrencyMixin):
    session: RobinhoodSession

    def get_crypto_holdings(self):
        raw_crypto_holdings = self._get_raw_crypto_holdings()
        crypto_holdings = []
        for raw_holding in raw_crypto_holdings:
            holding = CryptoHolding(raw_holding)
            crypto_holdings.append(holding)

        return CryptoHoldings(crypto_holdings)

    def _get_raw_crypto_holdings(self):
        first_page = self._get_first_crypto_holdings_page()
        all_pages = self.get_pages(first_page)
        raw_crypto_holdings = []
        for page in all_pages:
            for raw_holding in page.results:
                raw_crypto_holdings.append(raw_holding)

        return raw_crypto_holdings

    @auth_required
    def _get_first_crypto_holdings_page(self):
        endpoint = nummus.holdings()
        data = self.session.get_data(endpoint, timeout=15)
        return Page(data)

