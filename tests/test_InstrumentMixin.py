from RobinhoodTrader import RobinhoodTrader
from RobinhoodTrader.datatypes import Instrument, InstrumentList, Page


def test_get_instrument(trader):
    trader: RobinhoodTrader

    tesla = trader.get_instrument("TSLA")
    tesla = trader.get_instrument(tesla.id)
    tesla = trader.get_instrument(tesla.url)

    assert type(tesla) == Instrument


def test__get_first_instrument_page(trader):
    trader: RobinhoodTrader

    page = trader._get_first_instrument_page()

    assert type(page) == Page
