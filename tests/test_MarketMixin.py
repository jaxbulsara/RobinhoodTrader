from RobinhoodTrader import RobinhoodTrader
from RobinhoodTrader.datatypes import Market, MarketHours


def test_get_market(trader):
    trader: RobinhoodTrader

    market = trader.get_market("TSLA")
    market = trader.get_market(market.mic)

    expected_attributes = [
        "acronym",
        "city",
        "country",
        "mic",
        "name",
        "operating_mic",
        "timezone",
        "todays_hours",
        "url",
        "website",
    ]

    assert type(market) == Market

    for attribute in expected_attributes:
        assert hasattr(market, attribute)


def test_get_market_hours(trader):
    trader: RobinhoodTrader

    market = trader.get_market("TSLA")
    hours = trader.get_market_hours(market)

    expected_attributes = [
        "acronym",
        "city",
        "country",
        "mic",
        "name",
        "operating_mic",
        "timezone",
        "todays_hours",
        "url",
        "website",
    ]

    assert type(market) == Market

    for attribute in expected_attributes:
        assert hasattr(market, attribute)

