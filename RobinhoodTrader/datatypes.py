from __future__ import absolute_import
from collections import UserDict
from pprint import pformat


class RobinhoodData(UserDict):
    def __init__(self, *args, **kwargs):
        super(RobinhoodData, self).__init__(*args, **kwargs)

        # allow dictionary keys to be called as attributes of this object
        # eg data["key"] can be called as data.key
        self.__dict__.update(self.data)

    def __str__(self):
        return pformat(self.data, indent=4)


class Account(RobinhoodData):
    pass


class Cryptocurrency(RobinhoodData):
    pass


class CryptoAccount(RobinhoodData):
    pass


class CryptoWatchlist(RobinhoodData):
    pass


class CryptoHoldings(RobinhoodData):
    pass


class Instrument(RobinhoodData):
    pass


class Watchlist(RobinhoodData):
    pass


class Fundamentals(RobinhoodData):
    pass


class Market(RobinhoodData):
    pass


class Page(RobinhoodData):
    pass


class Positions(RobinhoodData):
    pass


class User(RobinhoodData):
    pass


class UserBasicInfo(RobinhoodData):
    pass


class UserAdditionalInfo(RobinhoodData):
    pass


class UserCipQuestions(RobinhoodData):
    pass


class UserEmployment(RobinhoodData):
    pass


class UserInvestmentProfile(RobinhoodData):
    pass


class Quote(RobinhoodData):
    pass
