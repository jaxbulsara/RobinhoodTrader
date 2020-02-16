from .Broker import Broker
from RobinhoodTrader import endpoints
from RobinhoodTrader.session import RobinhoodSession


class CryptoBroker(Broker):
    def getAccountID(self, session: RobinhoodSession):
        pass

    def getQuote(self, session: RobinhoodSession):
        pass
