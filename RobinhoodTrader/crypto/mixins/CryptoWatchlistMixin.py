from __future__ import absolute_import

from ...session import RobinhoodSession
from ...wrappers import auth_required
from ...endpoints import nummus
from ...datatypes import (
    RobinhoodDict,
    CryptoWatchlistList,
    CryptoWatchlist,
    Page,
)

from .CryptocurrencyMixin import CryptocurrencyMixin

import requests


class CryptoWatchlistMixin(CryptocurrencyMixin):
    session: RobinhoodSession

    def get_crypto_watchlist(self, name="Default"):
        page = self._get_first_crypto_watchlist_page()
        raw_watchlist = self.find_record(page, "name", name)

        return CryptoWatchlist(raw_watchlist)

    def get_all_crypto_watchlists(self):
        page = self._get_first_crypto_watchlist_page()
        all_pages = self.get_pages(page)
        all_watchlists = CryptoWatchlistList()
        for page in all_pages:
            for raw_watchlist in page.results:
                watchlist = CryptoWatchlist(raw_watchlist)
                all_watchlists.append(watchlist)

        return all_watchlists

    def get_crypto_watchlist_currency_pairs(self, watchlist=None):
        if watchlist is None:
            watchlist = self.get_crypto_watchlist()

        currency_pair_ids = watchlist.currency_pair_ids
        currency_pairs = list(
            map(
                lambda currency_pair_id: self.get_currency_pair(
                    currency_pair_id
                ),
                currency_pair_ids,
            )
        )

        return currency_pairs

    @auth_required
    def reorder_crypto_watchlist(
        self, reordered_currency_pairs, watchlist=None,
    ):
        if watchlist is None:
            watchlist = self.get_crypto_watchlist()

        reordered_currency_pair_ids = list(
            map(
                lambda currency_pair: currency_pair["id"],
                reordered_currency_pairs,
            )
        )

        watchlist_id = watchlist["id"]
        endpoint = nummus.watchlist_by_id(watchlist_id)
        payload = {"currency_pair_ids": reordered_currency_pair_ids}

        return self.session.patch_data(endpoint, json=payload, timeout=15,)

    def add_to_crypto_watchlist(self, currency_pair_to_add, watchlist=None):
        if watchlist is None:
            watchlist = self.get_crypto_watchlist()

        currency_pairs = self.get_crypto_watchlist_currency_pairs()
        currency_pairs.append(currency_pair_to_add)

        return self.reorder_crypto_watchlist(currency_pairs, watchlist)

    def add_multiple_to_crypto_watchlist(
        self, currency_pairs_to_add, watchlist=None
    ):
        if watchlist is None:
            watchlist = self.get_crypto_watchlist()

        currency_pairs = self.get_crypto_watchlist_currency_pairs()
        currency_pairs.append(currency_pairs_to_add)

        return self.reorder_crypto_watchlist(currency_pairs, watchlist)

    def delete_from_crypto_watchlist(
        self, currency_pair_to_delete, watchlist=None
    ):
        if watchlist is None:
            watchlist = self.get_crypto_watchlist()

        currency_pairs = self.get_crypto_watchlist_currency_pairs()
        try:
            currency_pairs.remove(currency_pair_to_delete)
        except ValueError:
            pass

        return self.reorder_crypto_watchlist(currency_pairs, watchlist)

    def delete_multiple_from_crypto_watchlist(
        self, currency_pairs_to_delete, watchlist=None
    ):
        if watchlist is None:
            watchlist = self.get_crypto_watchlist()

        currency_pairs = self.get_crypto_watchlist_currency_pairs()
        try:
            currency_pairs.remove(currency_pairs_to_delete)
        except ValueError:
            pass

        return self.reorder_crypto_watchlist(currency_pairs, watchlist)

    @auth_required
    def _get_first_crypto_watchlist_page(self):
        endpoint = nummus.watchlists()
        data = self.session.get_data(endpoint, timeout=15)
        return Page(data)
