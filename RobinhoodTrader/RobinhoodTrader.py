from RobinhoodTrader.utility import (
    LogFactory,
    Session,
    StockBroker,
    CryptoBroker,
)
from RobinhoodTrader.config import getConfiguration, getQrCode
import platform
import getpass


class RobinhoodTrader:
    def __init__(self, isVerbose=False):
        self.logFactory = LogFactory(isVerbose=isVerbose)
        self.log = self.logFactory.getLogger()
        self.config = getConfiguration()
        self.stockBroker = StockBroker()
        self.cryptoBroker = CryptoBroker()
        self.session = None

    def login(self, username=None, password=None):
        if username == None:
            username = input("Username: ")
            if platform.system() == "Windows":
                password = getpass.win_getpass(prompt="Password: ")
            else:
                password = getpass.getpass(prompt="Password: ")
        qrCode = getQrCode()
        self.session = Session()
        self.session.login(username, password, qrCode)
        self.stockBroker.addSession(self.session)
        self.cryptoBroker.addSession(self.session)

    def logout(self):
        self.session.logout()
        self.stockBroker.removeSession()
        self.cryptoBroker.removeSession()
