from RobinhoodTrader import RobinhoodTrader
from RobinhoodTrader.datatypes import Market, MarketHours


def test_get_market(trader):
    trader: RobinhoodTrader

    instrument = trader.get_instrument("TSLA")
    market = trader.get_market(instrument)
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

    instrument = trader.get_instrument("TSLA")
    market = trader.get_market(instrument)
    hours = trader.get_market_hours(market)

    expected_attributes = [
        "closes_at",
        "date",
        "extended_closes_at",
        "extended_opens_at",
        "is_open",
        "next_open_hours",
        "opens_at",
        "previous_open_hours",
    ]

    assert type(hours) == MarketHours

    for attribute in expected_attributes:
        assert hasattr(hours, attribute)

