from __future__ import absolute_import
from ..endpoints import nummus
from ..RobinhoodSession import RobinhoodSession
from .Pages import Pages


class Cryptocurrencies(Pages):
    session: RobinhoodSession

    def getFirstCurrencyPairPage(self) -> dict:
        response = self.session.get(nummus.currencyPairs(), timeout=15)
        response.raise_for_status()
        data = response.json()

        return data

    def getCurrencyPairBySymbol(self, currencyPairSymbol: str) -> dict:
        page = self.getFirstCurrencyPairPage()
        currencyPair = self.searchForRecord(page, "symbol", currencyPairSymbol)

        return currencyPair

    def getCurrencyPairById(self, currencyPairId: str) -> dict:
        page = self.getFirstCurrencyPairPage()
        currencyPair = self.searchForRecord(page, "id", currencyPairId)

        return currencyPair
