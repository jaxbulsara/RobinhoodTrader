from __future__ import absolute_import

import re


class ArgumentChecking:
    def check_argument(self, argument_name, argument, *required_types):
        argument_type = type(argument)
        required_types_message = ""

        for index, required_type in enumerate(list(required_types)):
            if index == 0:
                required_types_message += required_type.__name__
            else:
                required_types_message += f", {required_type}"

            if argument_type == required_type:
                return True

        message = f"'{argument_name}' must be {required_types_message}, not {argument_type.__name__}."
        raise TypeError(message)

    def is_symbol(self, symbol):
        symbol = symbol.upper()
        symbol_pattern = r"^[A-Z]+$"
        is_symbol = re.match(symbol_pattern, symbol) is not None
        return is_symbol

    def is_uuid(self, uuid):
        uuid = uuid.lower()
        id_pattern = (
            r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"
        )
        is_id = re.match(id_pattern, uuid) is not None
        return is_id

    def is_api_url(self, url):
        url = url.lower()
        url_pattern = r"^https://api.robinhood.com/(\S)*"
        is_url = re.match(url_pattern, url) is not None
        return is_url

    def is_nummus_url(self, url):
        url = url.lower()
        url_pattern = r"^https://nummus.robinhood.com/(\S)*"
        is_url = re.match(url_pattern, url) is not None
        return is_url
