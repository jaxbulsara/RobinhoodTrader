from __future__ import absolute_import

from ...common import CommonMixins
from ...session import RobinhoodSession
from ...endpoints import nummus
from ...exceptions import CategoryError
from ...datatypes import CurrencyPair, Page


class CryptocurrencyMixin(CommonMixins):
    session: RobinhoodSession

    def get_currency_pair(self, identifier):
        self.check_argument("identifier", identifier, str)
        currency_pair = self._get_currency_pair_by_category(identifier)

        return CurrencyPair(currency_pair)

    def _get_currency_pair_by_category(self, identifier):
        identifier_category = self.get_category("identifier", identifier)
        if identifier_category == "crypto_symbol":
            currency_pair = self._get_currency_pair_by_symbol(identifier)

        elif identifier_category == "uuid":
            currency_pair = self._get_currency_pair_by_id(identifier)

        else:
            raise CategoryError(
                f"'currency_pair' must be a crypto symbol or uuid, not {identifier_category}."
            )

        return currency_pair

    def _get_currency_pair_by_symbol(self, currencyPairSymbol: str) -> dict:
        page = self._get_first_currency_pair_page()
        return self.find_record(page, "symbol", currencyPairSymbol)

    def _get_currency_pair_by_id(self, currencyPairId: str) -> dict:
        page = self._get_first_currency_pair_page()
        return self.find_record(page, "id", currencyPairId)

    def _get_first_currency_pair_page(self) -> dict:
        endpoint = nummus.currency_pairs()
        data = self.session.get_data(endpoint, timeout=15)
        return Page(data)
