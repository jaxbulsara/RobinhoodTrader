from __future__ import absolute_import
from ..endpoints import api
from ..RobinhoodSession import RobinhoodSession
from ..wrappers import auth_required
from ..exceptions import CategoryError, IdentifierError
from .Pages import Pages
from .ArgumentChecker import ArgumentChecker
import requests
import re


class Instruments(Pages, ArgumentChecker):
    session: RobinhoodSession

    def get_instrument(self, identifier):
        identifier_type = type(identifier).__name__
        if identifier_type == "str":
            instrument = self._get_instrument_by_category(identifier)
        else:
            raise TypeError(
                f"'identifier' must be a (str). Got '{identifier_type}'."
            )
        return instrument

    def _get_instrument_by_category(self, identifier):
        if self.is_symbol(identifier):
            instrument = self._get_instrument_by_symbol(identifier)

        elif self.is_uuid(identifier):
            instrument = self._get_instrument_by_id(identifier)

        elif self.is_instrument_url(identifier):
            instrument = self._get_instrument_by_url(identifier)

        else:
            raise CategoryError(
                f"The instrument identifier must be a symbol, robinhood ID, or robinhood URL. Got '{identifier}'."
            )

        return instrument

    def _get_instrument_by_symbol(self, instrumentSymbol):
        endpoint = api.instrument_by_symbol(instrumentSymbol.upper())
        data = self.session.get_data(endpoint, timeout=15)
        try:
            instrument = data["results"][0]
        except IndexError:
            raise IdentifierError(
                f"Could not find instrument symbol '{instrumentSymbol}' at endpoint '{endpoint}'."
            )

        return instrument

    def _get_instrument_by_id(self, instrumentId):
        endpoint = api.instrument_by_id(instrumentId.lower())
        try:
            data = self.session.get_data(endpoint, timeout=15)
        except requests.exceptions.HTTPError as http_error:
            if http_error.response.status_code == 404:
                raise IdentifierError(
                    f"Could not find instrument id '{instrumentId}' at endpoint '{endpoint}'."
                )
            else:
                raise http_error
        return data

    def _get_instrument_by_url(self, instrumentUrl):
        endpoint = instrumentUrl
        endpoint = instrumentUrl
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
        return self.session.get_data(endpoint, timeout=15)

