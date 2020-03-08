from RobinhoodTrader import RobinhoodTrader
import pytest, uuid


def test__ArgumentChecking__check_argument(trader):
    trader: RobinhoodTrader

    with pytest.raises(TypeError):
        trader.check_argument("test", "test", list)

    with pytest.raises(TypeError):
        trader.check_argument("test", "test", int, float)

    assert trader.check_argument("test", "test", str)
    assert trader.check_argument("test", 1, int, float)
    assert trader.check_argument("test", 1.0, int, float)


def test_is_symbol(trader):
    trader: RobinhoodTrader

    assert trader.is_symbol("AAPL")
    assert trader.is_symbol("aapl")
    assert not trader.is_symbol("uuid-uuid")


def test_is_uuid(trader):
    trader: RobinhoodTrader

    assert trader.is_uuid(str(uuid.uuid4()))
    assert trader.is_uuid(str(uuid.uuid4()).upper())
    assert not trader.is_uuid("aapl")


def test_is_api_url(trader):
    trader: RobinhoodTrader

    assert trader.is_api_url("https://api.robinhood.com/instruments/",)
    assert trader.is_api_url("https://api.robinhood.com/instruments/",)
    assert not trader.is_api_url("aapl")


def test_is_nummus_url(trader):
    trader: RobinhoodTrader

    assert trader.is_nummus_url("https://nummus.robinhood.com/currency_pairs/")
    assert trader.is_nummus_url("https://nummus.robinhood.com/currency_pairs/")
    assert not trader.is_nummus_url("aapl")
