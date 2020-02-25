from __future__ import absolute_import
from ..endpoints import nummus
from ..RobinhoodSession import RobinhoodSession
from .Pages import Pages


class Cryptocurrencies(Pages):
    session: RobinhoodSession

    def getFirstCurrencyPairPage(self) -> dict:
        endpoint = nummus.currencyPairs()
        return self.session.getData(endpoint, timeout=15)

    def getCurrencyPairBySymbol(self, currencyPairSymbol: str) -> dict:
        page = self.getFirstCurrencyPairPage()
        currencyPair = self.searchForRecord(page, "symbol", currencyPairSymbol)

        return currencyPair

    def getCurrencyPairById(self, currencyPairId: str) -> dict:
        page = self.getFirstCurrencyPairPage()
        currencyPair = self.searchForRecord(page, "id", currencyPairId)

        return currencyPair
