from __future__ import absolute_import
from ..endpoints import api
from ..RobinhoodSession import RobinhoodSession
from ..wrappers import authRequired
from .Pages import Pages


class Instruments(Pages):
    session: RobinhoodSession

    def getFirstInstrumentPage(self) -> dict:
        endpoint = api.instruments()
        return self.session.getData(endpoint, timeout=15)

    def getInstrumentBySymbol(self, instrumentSymbol: str) -> dict:
        endpoint = api.instrumentBySymbol(instrumentSymbol)
        data = self.session.getData(endpoint, timeout=15)
        instrument = data["results"][0]

        return instrument

    def getInstrumentById(self, instrumentId: str) -> dict:
        endpoint = api.instrumentById(instrumentId)
        return self.session.get(endpoint, timeout=15)

    def getInstrumentByUrl(self, instrumentUrl: str) -> dict:
        endpoint = instrumentUrl
        return self.session.getData(endpoint, timeout=15)

    @authRequired
    def getFundamentalsByInstrument(self, instrument: dict) -> dict:
        endpoint = instrument["fundamentals"]
        return self.session.getData(endpoint, timeout=15)

    @authRequired
    def getFundamentalsBySymbol(self, symbol: str) -> dict:
        endpoint = api.fundamentalsBySymbol(symbol)
        return self.session.getData(endpoint, timeout=15)

    @authRequired
    def getQuoteByInstrument(self, instrument: dict) -> dict:
        endpoint = instrument["quote"]
        return self.session.getData(endpoint, timeout=15)

    @authRequired
    def getQuoteBySymbol(self, symbol: str) -> dict:
        endpoint = api.quoteBySymbol(symbol)
        return self.session.getData(endpoint, timeout=15)
