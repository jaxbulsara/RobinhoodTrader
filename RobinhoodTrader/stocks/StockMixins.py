from __future__ import absolute_import

from .mixins import (
    AccountMixin,
    FundamentalsMixin,
    MarketMixin,
    PositionsMixin,
    QuoteMixin,
)


class StockMixins(
    AccountMixin, FundamentalsMixin, MarketMixin, PositionsMixin, QuoteMixin,
):
    pass
