from __future__ import absolute_import

from ...exceptions import CategoryError

import re, uuid


class ArgumentCheckingMixin:
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

    def _is_symbol(self, argument):
        self.check_argument("argument", argument, str)
        argument = argument.upper()
        symbol_pattern = r"^[A-Z]+$"
        is_symbol = re.match(symbol_pattern, argument) is not None
        if is_symbol:
            return "symbol"
        else:
            return None

    def _is_crypto_symbol(self, argument):
        self.check_argument("argument", argument, str)
        argument = argument.upper()
        crypto_symbol_pattern = r"^([A-Z]+)-([A-Z]+)$"
        is_crypto_symbol = re.match(crypto_symbol_pattern, argument) is not None
        if is_crypto_symbol:
            return "crypto_symbol"
        else:
            return None

    def _is_uuid(self, argument):
        self.check_argument("argument", argument, str)
        argument_hex = argument.lower().replace("-", "")
        try:
            uuid.UUID(hex=argument_hex)
            return "uuid"
        except ValueError:
            return None

    def _is_api_url(self, argument):
        self.check_argument("argument", argument, str)
        argument = argument.lower()
        url_pattern = r"^https://api.robinhood.com/(\S)*"
        is_url = re.match(url_pattern, argument) is not None
        if is_url:
            return "api_url"
        else:
            return None

    def _is_nummus_url(self, argument):
        self.check_argument("argument", argument, str)
        argument = argument.lower()
        url_pattern = r"^https://nummus.robinhood.com/(\S)*"
        is_url = re.match(url_pattern, argument) is not None

        if is_url:
            return "nummus_url"
        else:
            return None
