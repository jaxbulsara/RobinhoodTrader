from .Broker import Broker
from RobinhoodTrader import endpoints


class StockBroker(Broker):
    def getInstruments(self, session, stockSymbol=None):
        pass
    
    def getInstrumentByStock(self, session, stockSymbol):
        pass

    def getInstrumentByID(self, session, stockID):
        pass




