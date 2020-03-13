from RobinhoodTrader import RobinhoodTrader
from RobinhoodTrader.datatypes import (
    CryptoWatchlistList,
    CryptoWatchlist,
    CurrencyPairIdList,
)


def test_get_crypto_watchlist(trader):
    trader: RobinhoodTrader

    default_watchlist = trader.get_crypto_watchlist()

    expected_attributes = [
        "created_at",
        "currency_pair_ids",
        "id",
        "name",
        "updated_at",
    ]

    assert type(default_watchlist) == CryptoWatchlist

    for attribute in expected_attributes:
        assert hasattr(default_watchlist, attribute)

    assert type(default_watchlist.currency_pair_ids) == CurrencyPairIdList

    for currency_pair in default_watchlist.currency_pair_ids:
        assert trader.get_category("currency_pair", currency_pair) == "uuid"


def test_get_all_crypto_watchlists(trader):
    trader: RobinhoodTrader

    all_watchlists = trader.get_all_crypto_watchlists()

    assert type(all_watchlists) == CryptoWatchlistList

    for watchlist in all_watchlists:
        assert type(watchlist) == CryptoWatchlist


def test_get_crypto_watchlist_currency_pairs(trader):
    trader: RobinhoodTrader

    watchlist_currency_pairs = trader.get_crypto_watchlist_currency_pairs()

