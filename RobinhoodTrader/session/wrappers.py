import requests


def authRequired(function):  # pylint: disable=E0213
    def makeUserLogin(self, session=None, *args, **kwargs):
        if session == None:
            session = self
        if not self.isLoggedIn:
            self.login(session.credentials)
        try:
            return function(self, *args, **kwargs)  # pylint: disable=E1102
        except requests.exceptions.HTTPError:
            print(f"You must login to use this method ({function.__name__}).")

    return makeUserLogin
