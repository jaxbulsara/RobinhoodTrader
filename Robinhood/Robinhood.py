from Robinhood.utility import LogFactory, Session
from Robinhood.config import getConfiguration
import getpass


class Robinhood:
    def __init__(self, isVerbose=False):
        self.logFactory = LogFactory(isVerbose=isVerbose)
        self.log = self.logFactory.getLogger()
        self.config = getConfiguration()
        self.session = None

    def login(self, username=None, password=None):
        if username == None:
            username = input("Username: ")
            password = getpass.win_getpass(prompt="Password: ")
        qrCode = self._getQrCode()
        self.session = Session()
        self.session.login(username, password, qrCode)

    def logout(self):
        pass

    def _getQrCode(self):
        try:
            qrCode = self.config["login"]["qrCode"]

        except KeyError:
            qrCode = None

        return qrCode
