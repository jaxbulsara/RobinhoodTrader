import re


class ArgumentChecker:
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
