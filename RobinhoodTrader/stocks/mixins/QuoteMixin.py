from __future__ import absolute_import

from ...session import RobinhoodSession
from ...wrappers import auth_required
from ...endpoints import api
from ...exceptions import IdentifierError
from ...datatypes import Quote, QuoteList, Instrument

from .InstrumentMixin import InstrumentMixin

import requests


class QuoteMixin(InstrumentMixin):
    session: RobinhoodSession

    def get_quote(self, identifier):
        identifier_type = self.check_argument(
            "identifier", identifier, Instrument, str
        )

        if identifier_type == Instrument:
            quote = self._get_quote_by_instrument(identifier)

        elif identifier_type == str:
            identifier_category = self.get_category("identifier", identifier)
            if identifier_category == "symbol":
                quote = self._get_quote_by_symbol(identifier)
            elif identifier_category == "uuid":
                quote = self._get_quote_by_instrument_id(identifier)

        quote.update({"trader": self, "instrument_url": quote["instrument"]})
        quote.pop("instrument")

        return Quote(quote)

    def get_multiple_quotes(self, identifier_list):
        self.check_argument("identifier_list", identifier_list, list)
        quote_list = list(
            map(lambda instrument: self.get_quote(instrument), identifier_list)
        )

        return QuoteList(quote_list)

    @auth_required
    def _get_quote_by_instrument(self, instrument):
        try:
            endpoint = instrument["quote_url"]
            return self.session.get_data(endpoint, timeout=15)
        except IndexError:
            raise ValueError(
                "'instrument' must be a robinhood instrument (dict)."
            )

    @auth_required
    def _get_quote_by_symbol(self, symbol):
        endpoint = api.quote_by_symbol(symbol)
        try:
            return self.session.get_data(endpoint, timeout=15)
        except requests.exceptions.HTTPError as http_error:
            if http_error.response.status_code == 404:
                raise IdentifierError(
                    f"Could not find fundamentals symbol '{symbol}' at endpoint '{endpoint}'."
                )
            else:
                raise http_error

    def _get_quote_by_instrument_id(self, instrument_id):
        instrument = self.get_instrument(instrument_id)
        return self._get_quote_by_instrument(instrument)
