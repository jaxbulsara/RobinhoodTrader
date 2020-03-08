from __future__ import absolute_import

from ...session import RobinhoodSession
from ...wrappers import auth_required
from ...endpoints import api
from ...exceptions import IdentifierError

from .InstrumentMixin import InstrumentMixin

import datetime, requests


class MarketMixin(InstrumentMixin):
    session: RobinhoodSession

    def get_market(self, identifier):
        identifierType = type(identifier).__name__
        if identifierType == "dict":
            market = self._get_market_by_instrument(identifier)
        if identifierType == "str":
            market = self._get_market_by_mic(identifier)
        else:
            raise TypeError(
                f"This method requires an instrument (dict) or market identifier code (str). Got '{identifierType}'"
            )

        return market

    @auth_required
    def get_market_hours(self, market, date=datetime.datetime.today()):
        inputType = type(market).__name__
        if inputType == "dict":
            market_hours = self._get_market_hours(market, date)

        elif inputType == "str":
            market_hours = self._get_market_hours_by_mic(market, date)
        else:
            raise TypeError(
                f"Argument must be a market (dict) or identifier code (str). Got '{inputType}'."
            )

        return market_hours

    @auth_required
    def _get_market_by_mic(self, mic):
        endpoint = api.market_by_mic(mic)
        try:
            market = self.session.get_data(endpoint, timeout=15)
        except requests.exceptions.HTTPError as http_error:
            if http_error.response.status_code == 404:
                raise IdentifierError(
                    f"Could not find market identifier code '{mic}' at endpoint '{endpoint}'."
                )
            else:
                raise http_error
        return market

    @auth_required
    def _get_market_by_instrument(self, instrument):
        try:
            endpoint = instrument["market"]
            return self.session.get_data(endpoint, timeout=15)
        except IndexError:
            raise ValueError("Argument must be an instrument (dict).")

    @auth_required
    def _get_first_market_page(self):
        endpoint = api.markets()
        return self.session.get_data(endpoint, timeout=15)

    @auth_required
    def _get_market_hours(self, market, date):
        date_type = type(date).__name__
        if date_type == "datetime.datetime":
            dateString = date.strftime("%Y-%m-%d")
            try:
                endpoint = api.market_hours_by_date(market["mic"], dateString)
                return self.session.get_data(endpoint, timeout=15)

            except IndexError:
                raise ValueError("'market' must be a robinhood market (dict).")

        else:
            raise TypeError(
                f"'date' must be a (datetime.datetime) object. Got '{date_type}'."
            )

    def _get_market_hours_by_mic(self, mic, date):
        mic_type = type(mic).__name__
        if mic_type == "str":
            market = self.get_market(mic)
            return self._get_market_hours(market, date)
        else:
            raise TypeError(
                f"'mic' must be a market identifier code (str). Got '{mic_type}'."
            )

