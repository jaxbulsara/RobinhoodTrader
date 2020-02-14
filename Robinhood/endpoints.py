apiUrl = "https://api.robinhood.com"


def login():
    return apiUrl + "/oauth2/token/"


def logout():
    return apiUrl + "/oauth2/revoke_token/"
