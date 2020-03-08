from __future__ import absolute_import

from .mixins import (
    AccountMixin,
    FundamentalsMixin,
    InstrumentWatchlistMixin,
    MarketMixin,
    PositionsMixin,
    QuoteMixin,
)


class StockMixins(
    AccountMixin,
    FundamentalsMixin,
    InstrumentWatchlistMixin,
    MarketMixin,
    PositionsMixin,
    QuoteMixin,
):
    pass
