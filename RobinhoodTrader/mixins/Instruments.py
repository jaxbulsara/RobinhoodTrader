from __future__ import absolute_import
from ..endpoints import api
from ..RobinhoodSession import RobinhoodSession
from ..wrappers import authRequired
from .Pages import Pages
from typing import Optional


class Instruments(Pages):
    session: RobinhoodSession

    def getFirstInstrumentPage(self) -> dict:
        endpoint = api.instruments()
        return self.session.getData(endpoint, timeout=15)

    def getInstrumentBySymbol(self, instrumentSymbol: str) -> Optional[dict]:
        endpoint = api.instrumentBySymbol(instrumentSymbol)
        data = self.session.getData(endpoint, timeout=15)
        try:
            instrument = data["results"][0]
        except IndexError:
            instrument = None

        return instrument

    def getInstrumentById(self, instrumentId: str) -> dict:
        endpoint = api.instrumentById(instrumentId)
        return self.session.get(endpoint, timeout=15)

    def getInstrumentByUrl(self, instrumentUrl: str) -> dict:
        endpoint = instrumentUrl
        return self.session.getData(endpoint, timeout=15)

