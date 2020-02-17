from .Broker import Broker
from RobinhoodTrader import nummusEndpoints
from RobinhoodTrader.session import RobinhoodSession
from RobinhoodTrader.session.wrappers import authRequired
import requests
from typing import List


class CryptoBroker(Broker):
    @authRequired
    def getAllWatchlists(self):
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

        response = self.session.get(nummusEndpoints.watchlists(), timeout=15)
        response.raise_for_status()
        data = response.json()

        return data

    def _watchlistNameOrDefault(self, watchlistName):
        allWatchlists = self.getAllWatchlists()
        if watchlistName is not None:
            if allWatchlists["next"]:
                nextUrl = allWatchlists["next"]
                watchlists = [allWatchlists["results"]]

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
                    if watchlistName == watchlist["name"]:

                        watchlistName = "Default"
        else:
            watchlistName = "Default"

        return watchlistName

    @authRequired
    def getWatchlist(self, watchlistName: str = None):
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

        watchlistName = self._watchlistNameOrDefault(watchlistName)
        allWatchlists = self.getAllWatchlists()

        if allWatchlists["next"]:
            nextUrl = allWatchlists["next"]

            while nextUrl:
                response = self.session.get(nextUrl, timeout=15)
                response.raise_for_status()
                data = response.json()
                watchlist = data["results"]

                if watchlistName == watchlist["name"]:
                    break

        else:
            watchlist = list(
                filter(
                    lambda watchlist: watchlist["name"] == watchlistName,
                    allWatchlists["results"],
                )
            )[0]

        return watchlist

    def getWatchlistCurrencyPairIds(self, watchlistName: str = None):
        """
        Example output:
        [   '3d961844-d360-45fc-989b-f6fca761d511',
            '76637d50-c702-4ed1-bcb5-5b0732a81f48',
            '383280b1-ff53-43fc-9c84-f01afd0989cd',
            '1ef78e1b-049b-4f12-90e5-555dcf2fe204']
        """
        watchlist = self.getWatchlist(watchlistName)
        instrumentIds = watchlist["currency_pair_ids"]

        return instrumentIds

    @authRequired
    def editWatchlist(
        self, currencyPairIds: List[str], watchlistName: str = None
    ):
        """
        Example Response Data:
        Same as getWatchlist()
        """
        watchlistName = self._watchlistNameOrDefault(watchlistName)
        watchlist = self.getWatchlist(watchlistName)
        watchlistID = watchlist["id"]
        headers = self.session.headers
        headers["Content-Type"] = "application/json"
        response = self.session.patch(
            nummusEndpoints.watchlistById(watchlistID),
            json={"currency_pair_ids": currencyPairIds},
            timeout=15,
        )
        response.raise_for_status()

        data = response.json()

        return data

    def addToWatchlist(
        self, currencyPairId: str, watchlistName: str = None,
    ):
        """
        Example Response Data:
        Same as getWatchlist()
        """
        watchlistName = self._watchlistNameOrDefault(watchlistName)
        watchlist = self.getWatchlist(watchlistName)
        currencyPairIds = watchlist["currency_pair_ids"]
        currencyPairIds.append(currencyPairId)
        data = self.editWatchlist(currencyPairIds, watchlistName)

        return data

    def addMultipleToWatchlist(
        self, currencyPairIdsToAdd: List[str], watchlistName: str = None,
    ):
        """
        Example Response Data:
        Same as getWatchlist()
        """
        watchlistName = self._watchlistNameOrDefault(watchlistName)
        watchlist = self.getWatchlist(watchlistName)
        currencyPairIds = watchlist["currency_pair_ids"]
        currencyPairIds.append(currencyPairIdsToAdd)
        data = self.editWatchlist(currencyPairIds, watchlistName)

        return data

    def deleteFromWatchlist(
        self, currencyPairId: str, watchlistName: str = None,
    ):
        """
        Example Response Data:
        Same as getWatchlist()
        """
        watchlistName = self._watchlistNameOrDefault(watchlistName)
        watchlist = self.getWatchlist(watchlistName)
        currencyPairIds = watchlist["currency_pair_ids"]
        currencyPairIds.remove(currencyPairId)
        data = self.editWatchlist(currencyPairIds, watchlistName)

        return data

    def deleteMultipleFromWatchlist(
        self, currencyPairIdsToDelete: List[str], watchlistName: str = None,
    ):
        """
        Example Response Data:
        Same as getWatchlist()
        """
        watchlistName = self._watchlistNameOrDefault(watchlistName)
        watchlist = self.getWatchlist(watchlistName)
        currencyPairIds = watchlist["currency_pair_ids"]
        for currencyPairId in currencyPairIdsToDelete:
            currencyPairIds.remove(currencyPairId)
        data = self.editWatchlist(currencyPairIds, watchlistName)

        return data

