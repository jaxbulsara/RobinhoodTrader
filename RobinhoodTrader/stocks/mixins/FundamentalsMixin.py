from __future__ import absolute_import

from ...session import RobinhoodSession
from ...wrappers import auth_required
from ...endpoints import api
from ...exceptions import IdentifierError
from ...datatypes import (
    Fundamentals,
    FundamentalsList,
    Instrument,
    InstrumentList,
)

from .InstrumentMixin import InstrumentMixin

import requests


class FundamentalsMixin(InstrumentMixin):
    session: RobinhoodSession

    def get_fundamentals(self, instrument):
        identifier_type = self.check_argument(
            "instrument", instrument, Instrument, str
        )

        if identifier_type == Instrument:
            fundamentals = self._get_fundamentals_by_instrument(instrument)

        elif identifier_type == str:
            identifier_category = self.get_category("instrument", instrument)
            if identifier_category == "symbol":
                fundamentals = self._get_fundamentals_by_symbol(instrument)

        return Fundamentals(fundamentals)

    def get_multiple_fundamentals(self, identifier_list):
        self.check_argument("identifier_list", identifier_list, list)
        fundamentals_list = list(
            map(
                lambda instrument: self.get_fundamentals(instrument),
                identifier_list,
            )
        )

        return FundamentalsList(fundamentals_list)

    @auth_required
    def _get_fundamentals_by_instrument(self, instrument):
        try:
            endpoint = instrument["_fundamentals"]
            return self.session.get_data(endpoint, timeout=15)
        except IndexError:
            raise ValueError(
                "'instrument' must be a robinhood instrument (dict)."
            )

    @auth_required
    def _get_fundamentals_by_symbol(self, symbol):
        endpoint = api.fundamentals_by_symbol(symbol)
        try:
            return self.session.get_data(endpoint, timeout=15)
        except requests.exceptions.HTTPError as http_error:
            if http_error.response.status_code == 404:
                raise IdentifierError(
                    f"Could not find fundamentals symbol '{symbol}' at endpoint '{endpoint}'."
                )
            else:
                raise http_error

