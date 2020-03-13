from RobinhoodTrader import RobinhoodTrader
from RobinhoodTrader.datatypes import Fundamentals, Page


def test_get_fundamentals(trader):
    trader: RobinhoodTrader

    tesla = trader.get_instrument("TSLA")

    fundamentals = trader.get_fundamentals("TSLA")
    fundamentals = trader.get_fundamentals(tesla)

    assert type(fundamentals) == Fundamentals


def test_get_multiple_fundamentals(trader):
    trader: RobinhoodTrader

    pass
