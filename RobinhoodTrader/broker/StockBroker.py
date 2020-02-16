from .Broker import Broker
from RobinhoodTrader import endpoints
from RobinhoodTrader.session import RobinhoodSession


class StockBroker(Broker):
    def getInstruments(self, session: RobinhoodSession, stockSymbol=None):
        pass

    def getInstrumentByStock(self, session: RobinhoodSession, stockSymbol):
        pass

    def getInstrumentByID(self, session: RobinhoodSession, stockID):
        pass

    def getQuote(self, session: RobinhoodSession):
        pass

