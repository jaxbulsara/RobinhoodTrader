from RobinhoodTrader import RobinhoodTrader
from RobinhoodTrader.datatypes import Instrument, InstrumentList, Page


def test_get_instrument(trader):
    trader: RobinhoodTrader

    tesla = trader.get_instrument("TSLA")
    tesla = trader.get_instrument(tesla.id)
    tesla = trader.get_instrument(tesla.url)

    expected_attributes = [
        "bloomberg_unique",
        "country",
        "day_trade_ratio",
        "default_collar_fraction",
        "fractional_tradability",
        "fundamentals_url",
        "id",
        "list_date",
        "maintenance_ratio",
        "margin_initial_ratio",
        "market_url",
        "min_tick_size",
        "name",
        "quote_url",
        "rhs_tradability",
        "simple_name",
        "splits",
        "state",
        "symbol",
        "tradability",
        "tradable_chain_id",
        "tradeable",
        "type",
        "url",
    ]

    assert type(tesla) == Instrument

    for attribute in expected_attributes:
        assert hasattr(tesla, attribute)


def test_get_multiple_instruments(trader):
    trader: RobinhoodTrader

    instrument_list = trader.get_multiple_instruments(["TSLA", "AAPL", "MSFT"])

    assert type(instrument_list) == InstrumentList

    for instrument in instrument_list:
        assert type(instrument) == Instrument


def test__get_first_instrument_page(trader):
    trader: RobinhoodTrader

    page = trader._get_first_instrument_page()

    assert type(page) == Page
