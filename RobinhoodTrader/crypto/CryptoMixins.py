from __future__ import absolute_import

from .mixins import (
    CryptoAccountMixin,
    CryptoHoldingsMixin,
)


class CryptoMixins(CryptoAccountMixin, CryptoHoldingsMixin):
    pass
