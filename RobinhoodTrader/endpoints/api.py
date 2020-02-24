from __future__ import absolute_import

api = "https://api.robinhood.com/"


def accounts():
    return api + "accounts/"


def accountUrl(accountNumber):
    return api + f"accounts/{accountNumber}/"


def accountPortfolio(accountNumber):
    return api + f"accounts/{accountNumber}/portfolio/"


def accountPositions(accountNumber):
    return api + f"accounts/{accountNumber}/positions/"


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
    return api + "fundamentals/"


def fundamentalsBySymbol(instrumentSymbol):
    return fundamentals() + instrumentSymbol + "/"


def historicals():
    return api + "quotes/historicals"


def instruments():
    return api + "instruments/"


def instrumentBySymbol(instrumentSymbol):
    return instruments() + "?symbol=" + instrumentSymbol


def instrumentById(instrumentId):
    return instruments() + instrumentId + "/"


def markets():
    return api + "markets/"


def marketBySymbol(instrumentSymbol):
    return markets() + instrumentSymbol + "/"


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


def positions():
    return api + "positions/"


def quotes():
    return api + "quotes/"


def quoteBySymbol(instrumentSymbol: str):
    return quotes() + instrumentSymbol + "/"


def tags():
    return api + "midland/tags/tag/"


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
