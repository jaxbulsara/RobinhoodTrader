from RobinhoodTrader import RobinhoodTrader
from RobinhoodTrader.exceptions import CategoryError
import pytest, uuid


def test__ArgumentChecking__check_argument(trader):
    trader: RobinhoodTrader

    with pytest.raises(
        TypeError, match=r"'(\S)+' must be (\w)+((, )*(\w)+)*, not (\w)+.",
    ):
        trader.check_argument("identifier", "test", list)

    with pytest.raises(
        TypeError, match=r"'(\S)+' must be (\w)+((, )*(\w)+)*, not (\w)+.",
    ):
        trader.check_argument("identifier", "test", int, float)

    assert trader.check_argument("identifier", "test", str)
    assert trader.check_argument("identifier", 1, int, float)
    assert trader.check_argument("identifier", 1.0, int, float)


def test_get_category(trader):
    trader: RobinhoodTrader

    assert trader.get_category("identifier", "AAPL") == "symbol"
    assert trader.get_category("identifier", "BTC-USD") == "crypto_symbol"
    assert trader.get_category("identifier", str(uuid.uuid4())) == "uuid"
    assert (
        trader.get_category(
            "identifier", "https://api.robinhood.com/instruments/",
        )
        == "api_url"
    )
    assert (
        trader.get_category(
            "identifier", "https://nummus.robinhood.com/currency_pairs/"
        )
        == "nummus_url"
    )

    with pytest.raises(
        TypeError, match=r"'(\S)+' must be (\w)+((, )*(\w)+)*, not (\w)+.",
    ):
        trader.get_category("identifier", 0)

    with pytest.raises(
        CategoryError,
        match=r"'(\S)+' must be a defined argument_category: [('(\S)+')+].",
    ):
        trader.get_category("identifier", "stock101!!")
