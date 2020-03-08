from __future__ import absolute_import

from .mixins import (
    CryptoAccountMixin,
    CryptoHoldingsMixin,
    CryptoWatchlistMixin,
)


class CryptoMixins(
    CryptoAccountMixin, CryptoHoldingsMixin, CryptoWatchlistMixin
):
    pass
