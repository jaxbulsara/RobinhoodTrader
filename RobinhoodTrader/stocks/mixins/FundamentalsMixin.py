from __future__ import absolute_import

from ...RobinhoodSession import RobinhoodSession
from ...wrappers import auth_required
from ...endpoints import api
from ...exceptions import IdentifierError

from .InstrumentMixin import InstrumentMixin

import requests


class FundamentalsMixin(InstrumentMixin):
    session: RobinhoodSession

    def get_fundamentals(self, instrument):
        instrumentType = type(instrument).__name__
        if instrumentType == "dict":
            return self._get_fundamentals_by_instrument(instrument)

        elif instrumentType == "str":
            return self._get_fundamentals_by_symbol(instrument)

        else:
            raise TypeError(
                f"Argument must be an instrument (dict) or instrument symbol (str). Got '{instrumentType}'."
            )

    def get_multiple_fundamentals(self, instruments):
        inputType = type(instruments).__name__
        if inputType == "list":
            fundamentals = list(
                map(
                    lambda instrument: self.get_fundamentals(instrument),
                    instruments,
                )
            )
        else:
            raise TypeError(
                f"Argument must be a list of instruments and/or instrument symbols (list). Got '{inputType}'."
            )

    @auth_required
    def _get_fundamentals_by_instrument(self, instrument):
        try:
            endpoint = instrument["fundamentals"]
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

