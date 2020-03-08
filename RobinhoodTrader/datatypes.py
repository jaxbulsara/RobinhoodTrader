from __future__ import absolute_import
from collections import UserDict


class Account(UserDict):
    pass


class Cryptocurrency(UserDict):
    pass


class CryptoAccount(UserDict):
    pass


class CryptoWatchlist(UserDict):
    pass


class CryptoHoldings(UserDict):
    pass


class Instrument(UserDict):
    pass


class Watchlist(UserDict):
    pass


class Fundamentals(UserDict):
    pass


class Market(UserDict):
    pass


class Page(UserDict):
    def __init__(self, data):
        super(Page, self).__init__(data)
        self.next = data["next"]
        self.results = data["results"]


class Positions(UserDict):
    pass


class User(UserDict):
    pass


class Quote(UserDict):
    pass
