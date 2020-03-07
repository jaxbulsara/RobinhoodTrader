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

    def is_symbol(self, identifier):
        identifier = identifier.upper()
        symbol_pattern = "^[A-Z]+$"
        is_symbol = re.match(symbol_pattern, identifier) is not None
        return is_symbol

    def is_uuid(self, identifier):
        identifier = identifier.lower()
        id_pattern = (
            "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"
        )
        is_id = re.match(id_pattern, identifier) is not None
        return is_id

    def is_instrument_url(self, identifier):
        identifier = identifier.lower()
        id_pattern = (
            "[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
        )
        url_pattern = f"^https://api.robinhood.com/instruments/{id_pattern}/$"
        is_url = re.match(url_pattern, identifier) is not None
        return is_url
