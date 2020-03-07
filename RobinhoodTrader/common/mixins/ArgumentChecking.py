from __future__ import absolute_import

import re


class ArgumentChecking:
    def checkArgument(self, argument_name, argument, *required_types):
        argument_type = type(argument)

        for required_type in required_types:
            if argument_type == required_type:
                return True

        message = f"'{argument_name}' must be {required_type.__name__}, not {argument_type.__name__}."
        raise TypeError(message)

    def is_symbol(self, identifier):
        identifier = identifier.upper()
        symbolPattern = "^[A-Z]+$"
        identifierIsSymbol = re.match(symbolPattern, identifier) is not None
        return identifierIsSymbol

    def is_uuid(self, identifier):
        identifier = identifier.lower()
        idPattern = (
            "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"
        )
        identifierIsId = re.match(idPattern, identifier) is not None
        return identifierIsId

    def is_instrument_url(self, identifier):
        identifier = identifier.lower()
        idPattern = (
            "[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
        )
        urlPattern = f"^https://api.robinhood.com/instruments/{idPattern}/$"
        identifierIsUrl = re.match(urlPattern, identifier) is not None
        return identifierIsUrl
