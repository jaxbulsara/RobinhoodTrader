api = "https://api.robinhood.com"


def login():
    return api + "/oauth2/token/"


def logout():
    return api + "/oauth2/revoke_token/"
