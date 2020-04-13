from RobinhoodTrader import RobinhoodTrader
from RobinhoodTrader.datatypes import Account, Instrument


def test_position(trader):
    trader: RobinhoodTrader

    position = trader.get_positions()[0]
    account = position.account()
    instrument = position.instrument()

    assert type(account) == Account
    assert type(instrument) == Instrument
