from __future__ import absolute_import
from .mixins import (
    Accounts,
    Fundamentals,
    InstrumentWatchlists,
    Markets,
    Positions,
    Quotes,
)


class StockTrader(
    Accounts, Fundamentals, InstrumentWatchlists, Markets, Positions, Quotes
):
    pass
