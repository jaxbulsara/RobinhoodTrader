from RobinhoodTrader import RobinhoodTrader
from RobinhoodTrader.datatypes import Positions, Position, Account, Instrument


def test_get_positions(trader):
    trader: RobinhoodTrader

    positions = trader.get_positions()

    assert type(positions) == Positions

    for position in positions:
        assert type(position) == Position


def test_position(trader):
    trader: RobinhoodTrader

    positions = trader.get_positions()
    position = positions[0]

    expected_attributes = [
        "account_url",
        "instrument_url",
        "account",
        "account_number",
        "average_buy_price",
        "created_at",
        "instrument",
        "intraday_average_buy_price",
        "intraday_quantity",
        "pending_average_buy_price",
        "quantity",
        "shares_held_for_buys",
        "shares_held_for_options_collateral",
        "shares_held_for_options_events",
        "shares_held_for_sells",
        "shares_held_for_stock_grants",
        "shares_pending_from_options_events",
        "updated_at",
        "url",
    ]

    assert type(position) == Position

    for attribute in expected_attributes:
        assert hasattr(position, attribute)


def test_position_account(trader):
    trader: RobinhoodTrader

    position = trader.get_positions()[0]
    account = position.account()

    assert type(account) == Account


def test_position_instrument(trader):
    trader: RobinhoodTrader

    position = trader.get_positions()[0]
    instrument = position.instrument()

    assert type(instrument) == Instrument

