import requests
from RobinhoodTrader import exceptions


def authRequired(function):  # pylint: disable=E0213
    def makeUserLogin(self, *args, **kwargs):
        if type(self).__name__ == "RobinhoodSession":
            session = self
        else:
            session = self.session
        if not session.isLoggedIn:
            session.login(session.credentials)
        return function(self, *args, **kwargs)  # pylint: disable=E1102

    return makeUserLogin
