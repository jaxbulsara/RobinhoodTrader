from __future__ import absolute_import
from .mixins import (
    User,
    Accounts,
    CryptoAccounts,
    Positions,
    Markets,
    Fundamentals,
    Quotes,
    InstrumentWatchlists,
    CryptoWatchlists,
    Printer,
)
from . import RobinhoodSession


class RobinhoodTrader(
    User,
    Accounts,
    CryptoAccounts,
    Positions,
    Markets,
    Fundamentals,
    Quotes,
    InstrumentWatchlists,
    CryptoWatchlists,
    Printer,
):
    def __init__(self):
        self.session = RobinhoodSession()

    def login(self, credentials=(None, None)):
        self.session.login(credentials)

    def logout(self):
        self.session.logout()
