from __future__ import absolute_import
from ..RobinhoodSession import RobinhoodSession
from ..endpoints import api
from ..wrappers import auth_required
from .Instruments import Instruments


class Quotes(Instruments):
    session: RobinhoodSession

    @auth_required
    def get_quote_by_instrument(self, instrument):
        endpoint = instrument["quote"]
        return self.session.get_data(endpoint, timeout=15)

    @auth_required
    def get_quote_by_symbol(self, symbol):
        instrument = self.get_instrument(symbol)
        quote = self.get_quote_by_instrument(instrument)
        return quote
