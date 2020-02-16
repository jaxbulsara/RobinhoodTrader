import requests
from RobinhoodTrader import exceptions


def authRequired(function):  # pylint: disable=E0213
    def makeUserLogin(self, *args, **kwargs):
        session = list(
            filter(lambda arg: type(arg).__name__ == "RobinhoodSession", args)
        )
        if session:
            session = session[0]
        else:
            session = self
        if not session.isLoggedIn:
            session.login(session.credentials)
        try:
            return function(self, *args, **kwargs)  # pylint: disable=E1102
        except requests.exceptions.HTTPError:
            raise exceptions.CredentialError

    return makeUserLogin
