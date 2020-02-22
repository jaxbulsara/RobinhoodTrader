from __future__ import absolute_import
from .mixins import (
    Account,
    StockWatchlist,
    CryptoWatchlist,
    Printer,
    Instruments,
)
from . import RobinhoodSession


class RobinhoodTrader(
    Account, StockWatchlist, CryptoWatchlist, Printer, Instruments,
):
    def __init__(self):
        self.session = RobinhoodSession()

    def login(self):
        self.session.login()

    def logout(self):
        self.session.logout()
