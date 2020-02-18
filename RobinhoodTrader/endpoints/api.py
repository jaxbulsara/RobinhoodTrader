from __future__ import absolute_import

api = "https://api.robinhood.com/"


def accounts():
    return api + "accounts/"


def accountByNumber(accountNumber):
    return accounts() + accountNumber + "/"


def accountPortfolio(accountNumber):
    return accountByNumber(accountNumber) + "/portfolio/"


def accountPositions(accountNumber):
    return accountByNumber(accountNumber) + "/positions/"


def forexQuotes():
    return api + "marketdata/forex/quotes/{}"


def forexHistoricals(symbol, interval=None, span=None, bounds=None):
    endpoint = api + f"marketdata/forex/historicals/{symbol}/"
    if interval:
        endpoint += f"?interval={interval}"
    if span:
        endpoint += f"?span={span}"
    if bounds:
        endpoint += f"?bounds={bounds}"

    return endpoint


def fundamentals():
    return api + "fundamentals/?symbols="


def historicals():
    return api + "quotes/historicals"


def markets():
    return api + "markets/"


def options():
    return api + "options/"


def optionPositions():
    return api + "options/positions/"


def optionOrders():
    return api + "options/orders"


def optionInstruments():
    return api + "options/instruments/"


def orders():
    return api + "orders/"


def portfolios():
    return api + "portfolios/"


def quotes():
    return api + "quotes/"


def tags():
    return api + "midland/tags/tag/"


def instruments():
    return api + "instruments/"


def token():
    return api + "/oauth2/token/"


def revokeToken():
    return api + "/oauth2/revoke_token/"


def user():
    return api + "user/"


def userAdditionalInfo():
    return api + "user/additional_info/"


def userBasicInfo():
    return api + "user/basic_info/"


def userCipQuestions():
    return api + "user/cip_questions/"


def userEmployment():
    return api + "user/employment/"


def userID():
    return api + "user/id/"


def userIdentityMismatch():
    return api + "user/identity_mismatch/"


def userInvestmentProfile():
    return api + "user/investment_profile/"


def watchlists():
    return api + f"watchlists/"


def watchlistByName(watchlistName: str = None):
    if watchlistName is None:
        watchlistName = "Default"
    return api + f"watchlists/{watchlistName}/"


def watchlistInstrument(instrumentID: str, watchlistName: str = None):
    return watchlistByName(watchlistName) + f"{instrumentID}/"


def watchlistReorder(watchlistName: str = None):
    return watchlistByName(watchlistName) + "reorder/"
