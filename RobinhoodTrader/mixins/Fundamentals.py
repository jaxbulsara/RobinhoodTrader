from __future__ import absolute_import
from ..RobinhoodSession import RobinhoodSession
from ..endpoints import api
from ..wrappers import authRequired
from .Instruments import Instruments
import datetime
from typing import List, Optional


class Fundamentals(Instruments):
    session: RobinhoodSession

    @authRequired
    def getFundamentalsByInstrument(self, instrument: dict) -> dict:
        endpoint = instrument["fundamentals"]
        return self.session.getData(endpoint, timeout=15)

    @authRequired
    def getFundamentalsBySymbol(self, instrumentSymbol: str) -> Optional[dict]:
        instrument = self.getInstrumentBySymbol(instrumentSymbol)
        if instrument is not None:
            fundamentals = self.getFundamentalsByInstrument(instrument)
        else:
            fundamentals = None
        return fundamentals

    @authRequired
    def getMultipleFundamentalsByInstrument(self, instruments: List[dict]):
        pass

    @authRequired
    def getMultipleFundamentalsBySymbol(self, symbols: List[str]):
        pass
