from RobinhoodTrader.session import RobinhoodSession
from RobinhoodTrader.broker import StockBroker, CryptoBroker


class RobinhoodTrader:
    def __init__(self, isVerbose=False):
        self.stockBroker = StockBroker()
        self.cryptoBroker = CryptoBroker()
        self.session = RobinhoodSession()

    def login(self, credentials=(None, None)):
        self.session.login(credentials)

    def logout(self):
        self.session.logout()

    def getInvestmentProfile(self):
        investmentProfile = self.stockBroker.getInvestmentProfile(self.session)
        return investmentProfile

    def getAllWatchlists(self):
        allWatchlists = self.stockBroker.getAllWatchlists(self.session)
        return allWatchlists

    def getWatchlist(self, watchlistName: str = "Default"):
        watchlist = self.stockBroker.getWatchlist(self.session, watchlistName)
        return watchlist

    def addToWatchList(self, instrumentUrl, watchlistName: str = "Default"):
        response = self.stockBroker.addToWatchlist(
            self.session, instrumentUrl, watchlistName
        )
        return response

    def deleteFromWatchlist(self, instrumentID, watchlistName: str = "Default"):
        response = self.stockBroker.deleteFromWatchlist(
            self.session, instrumentID, watchlistName
        )
        return response
