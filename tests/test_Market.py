from RobinhoodTrader import RobinhoodTrader
from RobinhoodTrader.datatypes import MarketHours


def test_market(trader):
    trader: RobinhoodTrader

    tesla = trader.get_instrument("TSLA")
    market = tesla.market()
    hours = market.hours()

    assert type(hours) == MarketHours
