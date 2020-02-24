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
    def getFirstCryptoWatchlistPage(self):
        """
        Example response:
        {   'next': None,
            'previous': None,
            'results': [   {'created_at': '2018-01-25T12:52:48.226482-05:00',
                            'currency_pair_ids': [  '3d961844-d360-45fc-989b-f6fca761d511',
                                                    '76637d50-c702-4ed1-bcb5-5b0732a81f48',
                                                    '383280b1-ff53-43fc-9c84-f01afd0989cd',
                                                    '1ef78e1b-049b-4f12-90e5-555dcf2fe204'],
                            'id': 'c339aa53-f02a-4f80-8cb0-2b3e49f49933',
                            'name': 'Default',
                            'updated_at': '2020-02-16T17:09:23.274835-05:00'}]}
        """

        response = self.session.get(nummus.watchlists(), timeout=15)
        response.raise_for_status()
        data = response.json()

        return data

    @authRequired
    def getCryptoWatchlist(self, watchlistName: str = "Default"):
        """
        Example response:
        {   'created_at': '2018-01-25T12:52:48.226482-05:00',
            'currency_pair_ids': [  '3d961844-d360-45fc-989b-f6fca761d511',
                                    '76637d50-c702-4ed1-bcb5-5b0732a81f48',
                                    '383280b1-ff53-43fc-9c84-f01afd0989cd',
                                    '1ef78e1b-049b-4f12-90e5-555dcf2fe204'],
            'id': 'c339aa53-f02a-4f80-8cb0-2b3e49f49933',
            'name': 'Default',
            'updated_at': '2020-02-16T17:09:23.274835-05:00'}
        """
        page = self.getFirstCryptoWatchlistPage()
        watchlist = self.searchForRecord(page, "name", watchlistName)

        return watchlist

    def getCryptoWatchlistCurrencyPairs(self, watchlist: List[dict]):
        """
        Example output:

        """
        if watchlist is None:
            watchlist = self.getCryptoWatchlist()
        currencyPairIds = watchlist["currency_pair_ids"]
        currencyPairs = []
        for currencyPairId in currencyPairIds:
            response = self.session.get(nummus.currencyPairById())

        return currencyPairIds

    @authRequired
    def editCryptoWatchlist(
        self, currencyPairIds: List[str], watchlist: List[dict]
    ):
        """
        Example Response Data:
        Same as getWatchlist()
        """
        watchlistName = self._watchlistNameOrDefault(watchlistName)
        watchlist = self.getCryptoWatchlist(watchlistName)
        watchlistID = watchlist["id"]
        headers = self.session.headers
        headers["Content-Type"] = "application/json"
        response = self.session.patch(
            nummus.watchlistById(watchlistID),
            json={"currency_pair_ids": currencyPairIds},
            timeout=15,
        )
        response.raise_for_status()

        data = response.json()

        return data

    def addToCryptoWatchlist(
        self, currencyPairId: str, watchlist: List[dict],
    ):
        """
        Example Response Data:
        Same as getWatchlist()
        """
        watchlistName = self._watchlistNameOrDefault(watchlistName)
        watchlist = self.getCryptoWatchlist(watchlistName)
        currencyPairIds = watchlist["currency_pair_ids"]
        currencyPairIds.append(currencyPairId)
        data = self.editCryptoWatchlist(currencyPairIds, watchlistName)

        return data

    def addMultipleToCryptoWatchlist(
        self, currencyPairIdsToAdd: List[str], watchlist: List[dict],
    ):
        """
        Example Response Data:
        Same as getWatchlist()
        """
        watchlistName = self._watchlistNameOrDefault(watchlistName)
        watchlist = self.getCryptoWatchlist(watchlistName)
        currencyPairIds = watchlist["currency_pair_ids"]
        currencyPairIds.append(currencyPairIdsToAdd)
        data = self.editCryptoWatchlist(currencyPairIds, watchlistName)

        return data

    def deleteFromCryptoWatchlist(
        self, currencyPairId: str, watchlist: List[dict],
    ):
        """
        Example Response Data:
        Same as getWatchlist()
        """
        watchlistName = self._watchlistNameOrDefault(watchlistName)
        watchlist = self.getCryptoWatchlist(watchlistName)
        currencyPairIds = watchlist["currency_pair_ids"]
        currencyPairIds.remove(currencyPairId)
        data = self.editCryptoWatchlist(currencyPairIds, watchlistName)

        return data

    def deleteMultipleFromCryptoWatchlist(
        self, currencyPairIdsToDelete: List[str], watchlist: List[dict],
    ):
        """
        Example Response Data:
        Same as getWatchlist()
        """
        watchlistName = self._watchlistNameOrDefault(watchlistName)
        watchlist = self.getCryptoWatchlist(watchlistName)
        currencyPairIds = watchlist["currency_pair_ids"]
        for currencyPairId in currencyPairIdsToDelete:
            currencyPairIds.remove(currencyPairId)
        data = self.editCryptoWatchlist(currencyPairIds, watchlistName)

        return data

    def _watchlistNameOrDefault(self, watchlistName):
        allWatchlists = self.getAllCryptoWatchlists()

        if watchlistName is not None:
            if allWatchlists["next"]:
                nextUrl = allWatchlists["next"]
                watchlists = [allWatchlists["results"][0]]

                while nextUrl:
                    response = self.session.get(nextUrl, timeout=15)
                    response.raise_for_status()
                    data = response.json()
                    watchlist = data["results"]
                    watchlists.append(watchlist)

                for watchlist in watchlists:
                    if watchlistName not in watchlist["name"]:
                        watchlistName = "Default"

            else:
                watchlists = allWatchlists["results"]

                for watchlist in watchlists:
                    if watchlistName not in watchlist["name"]:
                        watchlistName = "Default"
        else:
            watchlistName = "Default"

        return watchlistName
