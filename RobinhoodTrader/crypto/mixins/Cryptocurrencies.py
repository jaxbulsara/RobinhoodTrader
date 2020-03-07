from __future__ import absolute_import
from ...common import Common
from ...RobinhoodSession import RobinhoodSession
from ...endpoints import nummus
from ...exceptions import CategoryError


class Cryptocurrencies(Common):
    session: RobinhoodSession

    def get_currency_pair(self, identifier):
        identifierType = type(identifier).__name__
        if identifierType == "str":
            currency_pair = self._get_currency_pair_by_category(identifier)
        else:
            raise TypeError(
                f"This method requires an currency pair identifier (str). Got '{identifierType}'"
            )

        return currency_pair

    def _get_currency_pair_by_category(self, identifier):
        if self.is_symbol(identifier):
            currency_pair = self._get_currency_pair_by_symbol(identifier)

        elif self.is_uuid(identifier):
            currency_pair = self._get_currency_pair_by_id(identifier)

        else:
            raise CategoryError(
                f"The currency_pair identifier must be a symbol, robinhood ID, or robinhood URL. Got '{identifier}'."
            )

        return currency_pair

    def _get_currency_pair_by_symbol(self, currencyPairSymbol: str) -> dict:
        page = self._get_first_currency_pair_page()
        currencyPair = self.find_record(page, "symbol", currencyPairSymbol)

        return currencyPair

    def _get_currency_pair_by_id(self, currencyPairId: str) -> dict:
        page = self._get_first_currency_pair_page()
        currencyPair = self.find_record(page, "id", currencyPairId)

        return currencyPair

    def _get_first_currency_pair_page(self) -> dict:
        endpoint = nummus.currency_pairs()
        return self.session.get_data(endpoint, timeout=15)
