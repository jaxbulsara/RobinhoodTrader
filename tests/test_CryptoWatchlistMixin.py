from RobinhoodTrader import RobinhoodTrader
from RobinhoodTrader.datatypes import (
    CryptoWatchlistList,
    CryptoWatchlist,
    CurrencyPairIdList,
    CurrencyPair,
    CurrencyPairList,
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

    watchlist_currency_pair_list = (
        trader.get_crypto_watchlist_currency_pair_list()
    )

    assert type(watchlist_currency_pair_list) == CurrencyPairList

    for currency_pair in watchlist_currency_pair_list:
        assert type(currency_pair) == CurrencyPair


def test_reorder_crypto_watchlist(trader):
    trader: RobinhoodTrader

    original_currency_pair_list = (
        trader.get_crypto_watchlist_currency_pair_list()
    )

    first_currency_pair = original_currency_pair_list[0]
    reordered_currency_pair_list = original_currency_pair_list
    reordered_currency_pair_list.remove(first_currency_pair)
    reordered_currency_pair_list.append(first_currency_pair)

    trader.reorder_crypto_watchlist(reordered_currency_pair_list)

    reordered_currency_pairs_to_check = (
        trader.get_crypto_watchlist_currency_pair_list()
    )

    assert reordered_currency_pair_list == reordered_currency_pairs_to_check

    trader.reorder_crypto_watchlist(original_currency_pair_list)

    original_currency_pair_list_to_check = (
        trader.get_crypto_watchlist_currency_pair_list()
    )

    assert original_currency_pair_list == original_currency_pair_list_to_check


def test_add_to_remove_from_crypto_watchlist(trader):
    trader: RobinhoodTrader

    original_currency_pair_list = (
        trader.get_crypto_watchlist_currency_pair_list()
    )

    last_currency_pair = original_currency_pair_list[-1]

    expected_currency_list = original_currency_pair_list
    expected_currency_list.remove(last_currency_pair)

    print(original_currency_pair_list)

    # trader.remove_from_crypto_watchlist(last_currency_pair)
    # new_currency_pair_list = trader.get_crypto_watchlist_currency_pair_list()

    # assert new_currency_pair_list == expected_currency_list

    # trader.add_to_crypto_watchlist(last_currency_pair)
    # new_currency_pair_list = trader.get_crypto_watchlist_currency_pair_list()

    # assert new_currency_pair_list == original_currency_pair_list
