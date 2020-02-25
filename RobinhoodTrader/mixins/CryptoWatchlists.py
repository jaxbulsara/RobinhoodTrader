from __future__ import absolute_import
from ..RobinhoodSession import RobinhoodSession
from ..endpoints import nummus
from ..wrappers import authRequired
from .Cryptocurrencies import Cryptocurrencies

import requests
from typing import List, Optional


class CryptoWatchlists(Cryptocurrencies):
    session: RobinhoodSession

    @authRequired
    def getFirstCryptoWatchlistPage(self) -> dict:
        endpoint = nummus.watchlists()
        return self.session.getData(endpoint, timeout=15)

    def getCryptoWatchlist(self, watchlistName: str = "Default") -> dict:
        page = self.getFirstCryptoWatchlistPage()
        watchlist = self.searchForRecord(page, "name", watchlistName)

        return watchlist

    def getCryptoWatchlistCurrencyPairs(
        self, watchlist: Optional[dict] = None
    ) -> List[dict]:
        if watchlist is None:
            watchlist = self.getCryptoWatchlist()

        currencyPairIds = watchlist["currency_pair_ids"]
        currencyPairs = list(
            map(
                lambda currencyPairId: self.getCurrencyPairById(currencyPairId),
                currencyPairIds,
            )
        )

        return currencyPairs

    @authRequired
    def reorderCryptoWatchlist(
        self,
        reorderedCurrencyPairs: List[dict],
        watchlist: Optional[dict] = None,
    ) -> dict:
        if watchlist is None:
            watchlist = self.getCryptoWatchlist()

        reorderedCurrencyPairIds = list(
            map(lambda currencyPair: currencyPair["id"], reorderedCurrencyPairs)
        )

        watchlistID = watchlist["id"]
        endpoint = nummus.watchlistById(watchlistID)
        headers = self.session.headers
        headers["Content-Type"] = "application/json"
        payload = {"currency_pair_ids": reorderedCurrencyPairIds}

        data = self.session.patchData(endpoint, json=payload, timeout=15,)

        return data

    def addToCryptoWatchlist(
        self, currencyPairToAdd: dict, watchlist: Optional[dict] = None
    ):
        if watchlist is None:
            watchlist = self.getCryptoWatchlist()

        currencyPairs = self.getCryptoWatchlistCurrencyPairs()
        currencyPairs.append(currencyPairToAdd)

        data = self.reorderCryptoWatchlist(currencyPairs, watchlist)

        return data

    def addMultipleToCryptoWatchlist(
        self, currencyPairsToAdd: List[dict], watchlist: Optional[dict],
    ):
        if watchlist is None:
            watchlist = self.getCryptoWatchlist()

        currencyPairs = self.getCryptoWatchlistCurrencyPairs()
        currencyPairs.append(currencyPairsToAdd)

        data = self.reorderCryptoWatchlist(currencyPairs, watchlist)

        return data

    def deleteFromCryptoWatchlist(
        self, currencyPairToDelete: dict, watchlist: Optional[dict],
    ):
        if watchlist is None:
            watchlist = self.getCryptoWatchlist()

        currencyPairs = self.getCryptoWatchlistCurrencyPairs()
        currencyPairs.remove(currencyPairToDelete)
        data = self.reorderCryptoWatchlist(currencyPairs, watchlist)

        return data

    def deleteMultipleFromCryptoWatchlist(
        self, currencyPairsToDelete: List[dict], watchlist: Optional[dict],
    ):
        if watchlist is None:
            watchlist = self.getCryptoWatchlist()

        currencyPairs = self.getCryptoWatchlistCurrencyPairs()
        currencyPairs.remove(currencyPairsToDelete)
        data = self.reorderCryptoWatchlist(currencyPairs, watchlist)

        return data
