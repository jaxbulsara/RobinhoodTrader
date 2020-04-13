from RobinhoodTrader import RobinhoodTrader
from RobinhoodTrader.datatypes import Instrument, Fundamentals, Market, Quote
import pytest


@pytest.fixture
def test_instrument(trader):
    trader: RobinhoodTrader

    tesla = trader.get_instrument("TSLA")

    assert type(tesla) == Instrument

    yield tesla


def test_instrument_fundamentals(test_instrument):
    fundamentals = test_instrument.fundamentals()

    assert type(fundamentals) == Fundamentals


def test_instrument_market(test_instrument):
    market = test_instrument.market()

    assert type(market) == Market


def test_instrument_quote(test_instrument):
    quote = test_instrument.quote()

    assert type(quote) == Quote

