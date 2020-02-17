from RobinhoodTrader.session import RobinhoodSession
from RobinhoodTrader.broker import StockBroker, CryptoBroker
from typing import List, Tuple
from pprint import PrettyPrinter


class RobinhoodTrader:
    def __init__(self, isVerbose: bool = False):
        self.stockBroker = StockBroker()
        self.cryptoBroker = CryptoBroker()
        self.session = RobinhoodSession()
        self.printer = PrettyPrinter(indent=4)

    def login(self, credentials: Tuple[str] = (None, None)):
        self.session.login(credentials)
        self.stockBroker.addSession(self.session)
        self.cryptoBroker.addSession(self.session)

    def logout(self):
        self.session.logout()

    def printData(self, data):
        self.printer.pprint(data)
