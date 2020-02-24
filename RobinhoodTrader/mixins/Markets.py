from __future__ import absolute_import
from ..RobinhoodSession import RobinhoodSession
from ..endpoints import api
from ..wrappers import authRequired
from .Instruments import Instruments


class Markets(Instruments):
    session: RobinhoodSession

    @authRequired
    def getMarketBySymbol(self, symbol: str) -> dict:
        response = self.session.get(api.marketBySymbol(symbol), timeout=15)
        response.raise_for_status()
        data = response.json()

        return data

    @authRequired
    def getMarketByInstrument(self, instrument: dict) -> dict:
        response = self.session.get(instrument["market"], timeout=15)
        response.raise_for_status()
        data = response.json()

        return data
