from __future__ import absolute_import
from ..endpoints import api
from ..RobinhoodSession import RobinhoodSession
from ..wrappers import authRequired
from .Pages import Pages


class Instruments(Pages):
    session: RobinhoodSession

    def getFirstInstrumentPage(self) -> dict:
        response = self.session.get(api.instruments(), timeout=15)
        response.raise_for_status()
        data = response.json()

        return data

    def getInstrumentBySymbol(self, instrumentSymbol: str) -> dict:
        response = self.session.get(
            api.instrumentBySymbol(instrumentSymbol), timeout=15
        )
        response.raise_for_status()
        data = response.json()
        instrument = data["results"][0]

        return instrument

    def getInstrumentById(self, instrumentId: str) -> dict:
        response = self.session.get(
            api.instrumentById(instrumentId), timeout=15
        )
        response.raise_for_status()
        data = response.json()

        return data

    def getInstrumentByUrl(self, instrumentUrl: str) -> dict:
        response = self.session.get(instrumentUrl, timeout=15)
        response.raise_for_status()
        data = response.json()

        return data

    @authRequired
    def getFundamentalsByInstrument(self, instrument: dict) -> dict:
        response = self.session.get(instrument["fundamentals"], timeout=15)
        response.raise_for_status()
        data = response.json()

        return data

    @authRequired
    def getFundamentalsBySymbol(self, symbol: str) -> dict:
        response = self.session.get(
            api.fundamentalsBySymbol(symbol), timeout=15
        )
        response.raise_for_status()
        data = response.json()

        return data

    @authRequired
    def getQuoteByInstrument(self, instrument: dict) -> dict:
        response = self.session.get(instrument["quote"], timeout=15)
        response.raise_for_status()
        data = response.json()

        return data

    @authRequired
    def getQuoteBySymbol(self, symbol: str) -> dict:
        response = self.session.get(api.quoteBySymbol(symbol), timeout=15)
        response.raise_for_status()
        data = response.json()

        return data
