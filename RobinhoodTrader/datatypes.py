from __future__ import absolute_import

from RobinhoodTrader import RobinhoodTrader

from collections import UserDict, UserList
from pprint import pformat
import datetime


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
    def __init__(self, *args, **kwargs):
        super(Account, self).__init__(*args, **kwargs)
        if hasattr(self, "instant_eligibility"):
            self.instant_eligibility = InstantEligibility(
                self.instant_eligibility
            )

        if hasattr(self, "margin_balances"):
            self.margin_balances = MarginBalances(self.margin_balances)


class AccountList(RobinhoodList):
    pass


class CostBasisList(RobinhoodList):
    pass


class CostBasis(RobinhoodDict):
    pass


class CryptoAccount(RobinhoodDict):
    pass


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
        self.trader: RobinhoodTrader

    # @property
    # def quote(self):
    #     if type(self.fundamentals) == str:
    #         self.fundamentals = self.trader.get_crypto_quote(self)

    #     return self.fundamentals


class CurrencyPairList(RobinhoodList):
    pass


class CurrencyPairIdList(RobinhoodList):
    pass


class InstantEligibility(RobinhoodDict):
    pass


class Instrument(RobinhoodDict):
    trader: RobinhoodTrader

    def fundamentals(self):
        return self.trader.get_fundamentals(self)

    def market(self):
        return self.trader.get_market(self)

    def quote(self):
        return self.trader.get_quote(self)


class InstrumentList(RobinhoodList):
    pass


class Fundamentals(RobinhoodDict):
    pass


class FundamentalsList(RobinhoodList):
    pass


class MarginBalances(RobinhoodDict):
    pass


class Market(RobinhoodDict):
    trader: RobinhoodTrader

    def hours(self, date=datetime.datetime.today()):
        return self.trader.get_market_hours(self, date)


class MarketHours(RobinhoodDict):
    pass


class Page(RobinhoodDict):
    pass


class Position(RobinhoodDict):
    trader: RobinhoodTrader

    def account(self):
        account_number = self.account_url.split("/")[-2]
        return self.trader.get_account(account_number)

    def instrument(self):
        instrument_id = self.instrument_url.split("/")[-2]
        return self.trader.get_instrument(instrument_id)


class Positions(RobinhoodList):
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
    trader: RobinhoodTrader

    def instrument(self):
        instrument_id = self.instrument_url.split("/")[-2]
        return self.trader.get_instrument(instrument_id)


class QuoteList(RobinhoodList):
    pass
