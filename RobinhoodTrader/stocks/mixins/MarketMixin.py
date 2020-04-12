from __future__ import absolute_import

from ...session import RobinhoodSession
from ...wrappers import auth_required
from ...endpoints import api
from ...exceptions import IdentifierError
from ...datatypes import Instrument, Market, MarketHours

from .InstrumentMixin import InstrumentMixin

import datetime, requests


class MarketMixin(InstrumentMixin):
    session: RobinhoodSession

    def get_market(self, identifier):
        identifier_type = self.check_argument(
            "identifier", identifier, Instrument, str
        )

        if identifier_type == Instrument:
            market = self._get_market_by_instrument(identifier)

        elif identifier_type == str:
            identifier_category = self.get_category("identifier", identifier)
            if identifier_category == "symbol":
                market = self._get_market_by_mic(identifier)

        market.update({"trader": self})

        return Market(market)

    def get_market_hours(self, identifier, date=datetime.datetime.today()):
        identifier_type = self.check_argument(
            "identifier", identifier, Market, str
        )
        self.check_argument("date", date, datetime.datetime)
        if identifier_type == Market:
            market_hours = self._get_market_hours(identifier, date)

        elif identifier_type == str:
            identifier_category = self.get_category("identifier", identifier)
            if identifier_category == "symbol":
                market_hours = self._get_market_hours_by_mic(identifier, date)

        return MarketHours(market_hours)

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
            endpoint = instrument["_market"]
            return self.session.get_data(endpoint, timeout=15)
        except IndexError:
            raise ValueError("Argument must be an instrument (dict).")

    @auth_required
    def _get_first_market_page(self):
        endpoint = api.markets()
        return self.session.get_data(endpoint, timeout=15)

    @auth_required
    def _get_market_hours(self, market, date):
        dateString = date.strftime("%Y-%m-%d")
        endpoint = api.market_hours_by_date(market.mic, dateString)
        return self.session.get_data(endpoint, timeout=15)

    def _get_market_hours_by_mic(self, mic, date):
        market = self.get_market(mic)
        return self._get_market_hours(market, date)

