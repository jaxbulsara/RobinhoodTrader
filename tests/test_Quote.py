from RobinhoodTrader import RobinhoodTrader
from RobinhoodTrader.datatypes import Instrument


def test_quote(trader):
    trader: RobinhoodTrader

    quote = trader.get_quote("TSLA")
    instrument = quote.instrument()

    assert type(instrument) == Instrument
