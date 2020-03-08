from __future__ import absolute_import

from ...exceptions import CategoryError

import re


class ArgumentChecking:
    def check_argument(self, argument_name, argument, *required_types):
        argument_type = type(argument)
        required_types_message = ""

        for index, required_type in enumerate(list(required_types)):
            if index == 0:
                required_types_message += required_type.__name__
            else:
                required_types_message += f", {required_type.__name__}"

            if argument_type == required_type:
                return True

        message = f"'{argument_name}' must be {required_types_message}, not {argument_type.__name__}."
        raise TypeError(message)

    def get_category(self, argument_name, argument):
        available_categories = [
            "symbol",
            "crypto_symbol",
            "uuid",
            "api_url",
            "nummus_url",
        ]

        if argument_category := self._is_symbol(argument):
            return argument_category
        elif argument_category := self._is_crypto_symbol(argument):
            return argument_category
        elif argument_category := self._is_uuid(argument):
            return argument_category
        elif argument_category := self._is_api_url(argument):
            return argument_category
        elif argument_category := self._is_nummus_url(argument):
            return argument_category

        message = f"'{argument_name}' must be a defined argument_category: {available_categories}."
        raise CategoryError(message)

    def _is_symbol(self, symbol):
        self.check_argument("symbol", symbol, str)
        symbol = symbol.upper()
        symbol_pattern = r"^[A-Z]+$"
        is_symbol = re.match(symbol_pattern, symbol) is not None
        if is_symbol:
            return "symbol"
        else:
            return None

    def _is_crypto_symbol(self, symbol):
        self.check_argument("symbol", symbol, str)
        symbol = symbol.upper()
        crypto_symbol_pattern = r"^([A-Z]+)-([A-Z]+)$"
        is_crypto_symbol = re.match(crypto_symbol_pattern, symbol) is not None
        if is_crypto_symbol:
            return "crypto_symbol"
        else:
            return None

    def _is_uuid(self, uuid):
        self.check_argument("uuid", uuid, str)
        uuid = uuid.lower()
        id_pattern = (
            r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"
        )
        is_id = re.match(id_pattern, uuid) is not None
        if is_id:
            return "uuid"
        else:
            return None

    def _is_api_url(self, url):
        self.check_argument("url", url, str)
        url = url.lower()
        url_pattern = r"^https://api.robinhood.com/(\S)*"
        is_url = re.match(url_pattern, url) is not None
        if is_url:
            return "api_url"
        else:
            return None

    def _is_nummus_url(self, url):
        self.check_argument("url", url, str)
        url = url.lower()
        url_pattern = r"^https://nummus.robinhood.com/(\S)*"
        is_url = re.match(url_pattern, url) is not None

        if is_url:
            return "nummus_url"
        else:
            return None
