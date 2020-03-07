from __future__ import absolute_import
from .mixins import CryptoAccounts, CryptoHoldings, CryptoWatchlists


class CryptoTrader(CryptoAccounts, CryptoHoldings, CryptoWatchlists):
    pass
