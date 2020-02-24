from __future__ import absolute_import
from .mixins import (
    User,
    Accounts,
    CryptoAccounts,
    Markets,
    InstrumentWatchlists,
    CryptoWatchlists,
    Printer,
)
from . import RobinhoodSession
from typing import Tuple


class RobinhoodTrader(
    User,
    Accounts,
    CryptoAccounts,
    Markets,
    InstrumentWatchlists,
    CryptoWatchlists,
    Printer,
):
    def __init__(self):
        self.session = RobinhoodSession()

    def login(self, credentials: Tuple[str] = (None, None)):
        self.session.login(credentials)

    def logout(self):
        self.session.logout()
