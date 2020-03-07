from __future__ import absolute_import

nummus = "https://nummus.robinhood.com/"


def accounts():
    return nummus + "accounts/"


def account_by_id(accountId):
    return accounts() + accountId + "/"


def currency_pairs():
    return nummus + "currency_pairs/"


def currency_pair_by_symbol(symbol):
    return currency_pairs() + "?symbol=" + symbol


def holdings():
    return nummus + "holdings/"


def orders():
    return nummus + "orders/"


def order_status():
    return nummus + "orders/{}"


def order_cancel():
    return nummus + "orders/{}/cancel/"


def portfolios():
    return nummus + "portfolios/"


def watchlists():
    return nummus + "watchlists/"


def watchlist_by_id(id: str):
    return watchlists() + id + "/"
