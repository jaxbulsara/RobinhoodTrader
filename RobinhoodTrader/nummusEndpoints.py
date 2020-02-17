nummus = "https://nummus.robinhood.com/"


def accounts():
    return nummus + "accounts/"


def currencyPairs():
    return nummus + "currency_pairs"


def holdings():
    return nummus + "holdings/"


def orders():
    return nummus + "orders/"


def orderStatus():
    return nummus + "orders/{}"


def orderCancel():
    return nummus + "orders/{}/cancel/"


def portfolios():
    return nummus + "portfolios/"


def watchlists():
    return nummus + "watchlists/"


def watchlistById(watchlistId: str):
    return watchlists() + watchlistId + "/"
