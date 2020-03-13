from RobinhoodTrader import RobinhoodTrader
from RobinhoodTrader.exceptions import CategoryError
from RobinhoodTrader.datatypes import CurrencyPair, Currency, Page
import pytest


def test_get_currency_pair(trader):
    trader: RobinhoodTrader

    with pytest.raises(
        CategoryError,
        match=r"'currency_pair' must be a crypto symbol or uuid, not (\w)+.",
    ):
        trader.get_currency_pair("BTC")

    with pytest.raises(
        TypeError, match=r"'(\S)+' must be (\w)+((, )*(\w)+)*, not (\w)+.",
    ):
        trader.get_currency_pair(0)

    bitcoin = trader.get_currency_pair("BTC-USD")
    assert type(bitcoin) == CurrencyPair

    bitcoin = trader.get_currency_pair("3d961844-d360-45fc-989b-f6fca761d511")
    assert type(bitcoin) == CurrencyPair

    expected_attributes = [
        "asset_currency",
        "display_only",
        "id",
        "max_order_size",
        "min_order_price_increment",
        "min_order_quantity_increment",
        "min_order_size",
        "name",
        "quote_currency",
        "symbol",
        "tradability",
    ]

    expected_currency_keys = [
        "brand_color",
        "code",
        "id",
        "increment",
        "name",
        "type",
    ]

    assert type(bitcoin.asset_currency) == Currency
    assert type(bitcoin.quote_currency) == Currency

    for attribute in expected_attributes:
        assert hasattr(bitcoin, attribute)

    for key in bitcoin.asset_currency.keys():
        assert key in expected_currency_keys

    for key in bitcoin.quote_currency.keys():
        assert key in expected_currency_keys


def test__get_first_currency_pair_page(trader):
    trader: RobinhoodTrader

    first_currency_pair_page = trader._get_first_currency_pair_page()

    assert type(first_currency_pair_page) == Page
