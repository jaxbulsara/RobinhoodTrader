from __future__ import absolute_import
from .mixins import (
    Account,
    CryptoAccount,
    User,
    StockWatchlist,
    CryptoWatchlist,
    Printer,
)
from . import RobinhoodSession


class RobinhoodTrader(
    Account, CryptoAccount, User, StockWatchlist, CryptoWatchlist, Printer,
):
    def __init__(self):
        self.session = RobinhoodSession()

    def login(self):
        self.session.login()

    def logout(self):
        self.session.logout()
