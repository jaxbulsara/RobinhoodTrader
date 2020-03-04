from __future__ import absolute_import
from ..RobinhoodSession import RobinhoodSession
from ..endpoints import api
from ..wrappers import authRequired
from .Instruments import Instruments
import datetime
from typing import Optional


class Quotes(Instruments):
    session: RobinhoodSession

    @authRequired
    def getQuoteByInstrument(self, instrument: dict) -> dict:
        endpoint = instrument["quote"]
        return self.session.getData(endpoint, timeout=15)

    @authRequired
    def getQuoteBySymbol(self, instrumentSymbol: str) -> Optional[dict]:
        instrument = self.getInstrumentBySymbol(instrumentSymbol)
        if instrument is not None:
            quote = self.getQuoteByInstrument(instrument)
        else:
            quote = None
        return quote
