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
        watchlists = self.stockBroker.getAllWatchlists(self.session)
        return watchlists

    def getWatchlistByName(self, watchlistName):
        watchlist = self.stockBroker.getWatchlist(self.session, watchlistName)
        return watchlist
