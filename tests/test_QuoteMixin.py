from RobinhoodTrader import RobinhoodTrader
from RobinhoodTrader.datatypes import Quote, QuoteList


def test_get_quote(trader):
    trader: RobinhoodTrader

    tesla = trader.get_instrument("TSLA")
    quote = trader.get_quote(tesla)
    quote = trader.get_quote("TSLA")

    expected_attributes = [
        "adjusted_previous_close",
        "ask_price",
        "ask_size",
        "bid_price",
        "bid_size",
        "has_traded",
        "instrument_url",
        "last_extended_hours_trade_price",
        "last_trade_price",
        "last_trade_price_source",
        "previous_close",
        "previous_close_date",
        "symbol",
        "trader",
        "trading_halted",
        "updated_at",
    ]

    assert type(quote) == Quote

    for attribute in expected_attributes:
        assert hasattr(quote, attribute)


def test_get_multiple_quotes(trader):
    trader: RobinhoodTrader

    quotes = trader.get_multiple_quotes(["MSFT", "TSLA", "AAPL"])

    assert type(quotes) == QuoteList

    for quote in quotes:
        assert type(quote) == Quote
