from RobinhoodTrader.session import RobinhoodSession
from RobinhoodTrader.broker import StockBroker, CryptoBroker
from typing import List, Tuple


class RobinhoodTrader:
    def __init__(self, isVerbose: bool = False):
        self.stockBroker = StockBroker()
        self.cryptoBroker = CryptoBroker()
        self.session = RobinhoodSession()

    def login(self, credentials: Tuple[str] = (None, None)):
        self.session.login(credentials)
        self.stockBroker.addSession(self.session)
        self.cryptoBroker.addSession(self.session)

    def logout(self):
        self.session.logout()

    def getInvestmentProfile(self):
        investmentProfile = self.stockBroker.getInvestmentProfile()
        return investmentProfile

    def getAllWatchlists(self):
        allWatchlists = self.stockBroker.getAllWatchlists()
        return allWatchlists

    def getWatchlist(self, watchlistName: str = None):
        watchlist = self.stockBroker.getWatchlist(watchlistName)
        return watchlist

    def addToWatchList(self, instrumentUrl: str, watchlistName: str = None):
        response = self.stockBroker.addToWatchlist(instrumentUrl, watchlistName)
        return response

    def addMultipleToWatchlist(
        self, instrumentUrls: List[str], watchlistName: str = None
    ):
        response = self.stockBroker.addMultipleToWatchlist(
            instrumentUrls, watchlistName
        )
        return response

    def deleteFromWatchlist(self, instrumentID: str, watchlistName: str = None):
        response = self.stockBroker.deleteFromWatchlist(
            instrumentID, watchlistName
        )
        return response

    def deleteMultipleFromWatchlist(
        self, instrumentIds: List[str], watchlistName: str = None
    ):
        response = self.stockBroker.deleteMultipleFromWatchlist(
            instrumentIds, watchlistName
        )
        return response

    def getWatchlistInstrumentUrls(self, watchlistName: str = None):
        instrumentUrls = self.stockBroker.getWatchlistInstrumentUrls(
            watchlistName
        )
        return instrumentUrls

    def getWatchlistInstrumentIds(self, watchlistName: str = None):
        instrumentIds = self.stockBroker.getWatchlistInstrumentIds(
            watchlistName
        )
        return instrumentIds

    def reorderWatchList(
        self, instrumentIds: List[str], watchlistName: str = None
    ):
        response = self.stockBroker.reorderWatchList(
            instrumentIds, watchlistName
        )
        return response
