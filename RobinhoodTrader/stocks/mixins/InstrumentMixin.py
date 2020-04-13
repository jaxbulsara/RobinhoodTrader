from __future__ import absolute_import

from ...common import CommonMixins
from ...session import RobinhoodSession
from ...wrappers import auth_required
from ...endpoints import api
from ...exceptions import IdentifierError, CategoryError
from ...datatypes import Page, Instrument, InstrumentList

import re, requests


class InstrumentMixin(CommonMixins):
    session: RobinhoodSession

    def get_instrument(self, instrument_identifier):
        self.check_argument("instrument_identifier", instrument_identifier, str)
        instrument = self._get_instrument_by_category(instrument_identifier)

        instrument.update(
            {
                "trader": self,
                "fundamentals_url": instrument["fundamentals"],
                "market_url": instrument["market"],
                "quote_url": instrument["quote"],
            }
        )

        instrument.pop("fundamentals")
        instrument.pop("market")
        instrument.pop("quote")

        return Instrument(instrument)

    def get_multiple_instruments(self, instrument_identifier_list):
        self.check_argument(
            "instrument_identifier_list", instrument_identifier_list, list
        )
        instrument_list = list(
            map(
                lambda instrument_identifier: self.get_instrument(
                    instrument_identifier
                ),
                instrument_identifier_list,
            )
        )

        return InstrumentList(instrument_list)

    def _get_instrument_by_category(self, instrument_identifier):
        identifier_category = self.get_category(
            "instrument_identifier", instrument_identifier
        )
        if identifier_category == "symbol":
            return self._get_instrument_by_symbol(instrument_identifier)

        elif identifier_category == "uuid":
            return self._get_instrument_by_id(instrument_identifier)

        elif identifier_category == "api_url":
            return self._get_instrument_by_url(instrument_identifier)

    def _get_instrument_by_symbol(self, instrument_symbol):
        endpoint = api.instrument_by_symbol(instrument_symbol.upper())
        data = self.session.get_data(endpoint, timeout=15)
        try:
            instrument = data["results"][0]
        except IndexError:
            raise IdentifierError(
                f"Could not find instrument symbol '{instrument_symbol}' at endpoint '{endpoint}'."
            )

        return instrument

    def _get_instrument_by_id(self, instrument_id):
        endpoint = api.instrument_by_id(instrument_id.lower())
        try:
            data = self.session.get_data(endpoint, timeout=15)
        except requests.exceptions.HTTPError as http_error:
            if http_error.response.status_code == 404:
                raise IdentifierError(
                    f"Could not find instrument id '{instrument_id}' at endpoint '{endpoint}'."
                )
            else:
                raise http_error
        return data

    def _get_instrument_by_url(self, instrument_url):
        endpoint = instrument_url
        endpoint = instrument_url
        try:
            data = self.session.get_data(endpoint, timeout=15)
        except requests.exceptions.HTTPError as httpError:
            if httpError.response.status_code == 404:
                raise IdentifierError(
                    f"Could not find instrument at url '{endpoint}'."
                )
            else:
                raise httpError
        return data

    def _get_first_instrument_page(self):
        endpoint = api.instruments()
        data = self.session.get_data(endpoint, timeout=15)
        return Page(data)

