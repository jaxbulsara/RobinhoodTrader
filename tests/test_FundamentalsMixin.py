from RobinhoodTrader import RobinhoodTrader
from RobinhoodTrader.datatypes import Fundamentals, FundamentalsList, Page


def test_get_fundamentals(trader):
    trader: RobinhoodTrader

    tesla = trader.get_instrument("TSLA")

    fundamentals = trader.get_fundamentals("TSLA")
    fundamentals = trader.get_fundamentals(tesla)

    expected_attributes = [
        "average_volume",
        "average_volume_2_weeks",
        "ceo",
        "description",
        "dividend_yield",
        "float",
        "headquarters_city",
        "headquarters_state",
        "high",
        "high_52_weeks",
        "industry",
        "instrument",
        "low",
        "low_52_weeks",
        "market_cap",
        "num_employees",
        "open",
        "pb_ratio",
        "pe_ratio",
        "sector",
        "shares_outstanding",
        "volume",
        "year_founded",
    ]

    assert type(fundamentals) == Fundamentals

    for attribute in expected_attributes:
        assert hasattr(fundamentals, attribute)


def test_get_multiple_fundamentals(trader):
    trader: RobinhoodTrader

    fundamentals_list = trader.get_multiple_fundamentals(
        ["TSLA", "AAPL", "MSFT"]
    )

    assert type(fundamentals_list) == FundamentalsList

    for fundamentals in fundamentals_list:
        assert type(fundamentals) == Fundamentals
