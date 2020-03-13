from __future__ import absolute_import

from collections import UserDict, UserList
from pprint import pformat


class RobinhoodDict(UserDict):
    def __init__(self, *args, **kwargs):
        super(RobinhoodDict, self).__init__(*args, **kwargs)

        # allow dictionary keys to be called as attributes of this object
        # eg data["key"] can be called as data.key
        self.__dict__.update(self.data)

    def __str__(self):
        return pformat(self.data, indent=4)


class RobinhoodList(UserList):
    def __init__(self, *args, **kwargs):
        super(RobinhoodList, self).__init__(*args, **kwargs)

    def __str__(self):
        return pformat(self.data, indent=4)


class Account(RobinhoodDict):
    pass


class CostBasisList(RobinhoodList):
    pass


class CostBasis(RobinhoodDict):
    pass


class CryptoAccount(RobinhoodDict):
    pass


class CryptoWatchlistList(RobinhoodList):
    pass


class CryptoWatchlist(RobinhoodDict):
    def __init__(self, *args, **kwargs):
        super(CryptoWatchlist, self).__init__(*args, **kwargs)
        self.currency_pair_ids = CurrencyPairIdList(self.currency_pair_ids)


class CryptoHoldings(RobinhoodDict):
    def __init__(self, *args, **kwargs):
        super(CryptoHoldings, self).__init__(*args, **kwargs)
        self.cost_bases = CostBasisList(
            list(map(lambda cost_basis: CostBasis(cost_basis), self.cost_bases))
        )
        self.currency = Currency(self.currency)


class CryptoHoldingsList(RobinhoodList):
    pass


class Currency(RobinhoodDict):
    pass


class CurrencyPair(RobinhoodDict):
    def __init__(self, *args, **kwargs):
        super(CurrencyPair, self).__init__(*args, **kwargs)
        self.asset_currency = Currency(self.asset_currency)
        self.quote_currency = Currency(self.quote_currency)


class CurrencyPairList(RobinhoodList):
    pass


class CurrencyPairIdList(RobinhoodList):
    pass


class Instrument(RobinhoodDict):
    pass


class Watchlist(RobinhoodDict):
    pass


class Fundamentals(RobinhoodDict):
    pass


class Market(RobinhoodDict):
    pass


class Page(RobinhoodDict):
    pass


class Positions(RobinhoodDict):
    pass


class User(RobinhoodDict):
    pass


class UserBasicInfo(RobinhoodDict):
    pass


class UserAdditionalInfo(RobinhoodDict):
    pass


class UserCipQuestions(RobinhoodDict):
    pass


class UserEmployment(RobinhoodDict):
    pass


class UserInvestmentProfile(RobinhoodDict):
    pass


class Quote(RobinhoodDict):
    pass
