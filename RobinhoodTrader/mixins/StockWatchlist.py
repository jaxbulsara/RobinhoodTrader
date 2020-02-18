from __future__ import absolute_import
from ..RobinhoodSession import RobinhoodSession
from ..endpoints import api
from ..wrappers import authRequired

import requests
from typing import List, Callable


class StockWatchlist:
    session: RobinhoodSession

    @authRequired
    def getAllWatchlists(self):
        """
        Example response:
        {   'next': None,
            'previous': None,
            'results': [   {   'name': 'Default',
                            'url': 'https://api.robinhood.com/watchlists/Default/',
                            'user': 'api.robinhood.com/user/'}]} 
        """

        response = self.session.get(api.watchlists(), timeout=15)
        response.raise_for_status()
        data = response.json()

        return data

    @authRequired
    def getWatchlist(self, watchlistName: str = None):
        """
        Example response:
        [   {   'created_at': '2019-03-12T08:22:45.386349Z',
                'instrument': 'https://api.robinhood.com/instruments/50810c35-d215-4866-9758-0ada4ac79ffa/',
                'url': 'https://api.robinhood.com/watchlists/Default/50810c35-d215-4866-9758-0ada4ac79ffa/',
                'watchlist': 'https://api.robinhood.com/watchlists/Default/'},
            {   'created_at': '2019-03-12T08:23:12.96730Z',
                'instrument': 'https://api.robinhood.com/instruments/450dfc6d-5510-4d40-abfb-f633b7d9be3e/',
                'url': 'https://api.robinhood.com/watchlists/Default/450dfc6d-5510-4d40-abfb-f633b7d9be3e/',
                'watchlist': 'https://api.robinhood.com/watchlists/Default/'},
            {   'created_at': '2019-03-12T08:23:37.65831Z',
                'instrument': 'https://api.robinhood.com/instruments/943c5009-a0bb-4665-8cf4-a95dab5874e4/',
                'url': 'https://api.robinhood.com/watchlists/Default/943c5009-a0bb-4665-8cf4-a95dab5874e4/',
                'watchlist': 'https://api.robinhood.com/watchlists/Default/'},
            ]
        """
        watchlistName = self._watchlistNameOrDefault(watchlistName)
        response = self.session.get(
            api.watchlistByName(watchlistName), timeout=15
        )
        response.raise_for_status()
        data = response.json()["results"]

        return data

    def getWatchlistInstrumentUrls(self, watchlistName: str = None):
        """
        Example Output:
        [   'https://api.robinhood.com/instruments/e39ed23a-7bd1-4587-b060-71988d9ef483/',
            'https://api.robinhood.com/instruments/54db869e-f7d5-45fb-88f1-8d7072d4c8b2/',
            'https://api.robinhood.com/instruments/50810c35-d215-4866-9758-0ada4ac79ffa/',
            'https://api.robinhood.com/instruments/450dfc6d-5510-4d40-abfb-f633b7d9be3e/']  
        """
        watchlist = self.getWatchlist(watchlistName)
        instrumentUrls = list(
            map(lambda watchlistItem: watchlistItem["instrument"], watchlist)
        )

        return instrumentUrls

    def getWatchlistInstrumentIds(self, watchlistName: str = None):
        """
        Example Output:
        [   'e39ed23a-7bd1-4587-b060-71988d9ef483',
            '54db869e-f7d5-45fb-88f1-8d7072d4c8b2',
            '50810c35-d215-4866-9758-0ada4ac79ffa',
            '450dfc6d-5510-4d40-abfb-f633b7d9be3e']
        """
        instrumentUrls = self.getWatchlistInstrumentUrls(watchlistName)
        instrumentIds = list(
            map(
                lambda instrumentUrl: self.getInstrumentIdFromUrl(
                    instrumentUrl
                ),
                instrumentUrls,
            )
        )

        return instrumentIds

    def getInstrumentIdFromUrl(self, instrumentUrl):
        instrumentId = instrumentUrl.rstrip("/").split("/")[-1]
        return instrumentId

    @authRequired
    def addToWatchlist(
        self, instrumentUrl: str, watchlistName: str = None,
    ):
        """
        Example Response Data:
        {   'created_at': '2020-02-16T22:56:18.685673Z',
            'instrument': 'https://api.robinhood.com/instruments/f4d089b7-c822-48ac-884d-8ecb312ebb67/',
            'url': 'https://api.robinhood.com/watchlists/Default/f4d089b7-c822-48ac-884d-8ecb312ebb67/',
            'watchlist': 'https://api.robinhood.com/watchlists/Default/'}
        """
        watchlistName = self._watchlistNameOrDefault(watchlistName)
        try:
            response = self.session.post(
                api.watchlistByName(watchlistName),
                data={"instrument": instrumentUrl},
                timeout=15,
            )
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            print(
                f"Cannot add instrument. URL already exists: {api.watchlistInstrument(self.getInstrumentIdFromUrl, watchlistName)}"
            )

        data = response.json()

        return data

    def addMultipleToWatchlist(
        self, instrumentUrls: List[str], watchlistName: str = None
    ):
        """
        Example Response Data:
        [   {   'created_at': '2020-02-17T01:12:58.590500Z',
                'instrument': 'https://api.robinhood.com/instruments/e39ed23a-7bd1-4587-b060-71988d9ef483/',
                'url': 'https://api.robinhood.com/watchlists/Default/e39ed23a-7bd1-4587-b060-71988d9ef483/',
                'watchlist': 'https://api.robinhood.com/watchlists/Default/'},
            {   'created_at': '2020-02-17T01:12:58.736878Z',
                'instrument': 'https://api.robinhood.com/instruments/54db869e-f7d5-45fb-88f1-8d7072d4c8b2/',
                'url': 'https://api.robinhood.com/watchlists/Default/54db869e-f7d5-45fb-88f1-8d7072d4c8b2/',
                'watchlist': 'https://api.robinhood.com/watchlists/Default/'}]
        """
        response = list(
            map(
                lambda instrumentUrl: self.addToWatchlist(instrumentUrl),
                instrumentUrls,
            )
        )

        return response

    @authRequired
    def deleteFromWatchlist(
        self, instrumentID: str, watchlistName: str = None,
    ):
        """
        Example Response Data:
        <Response [204]>
        """
        watchlistName = self._watchlistNameOrDefault(watchlistName)
        try:
            response = self.session.delete(
                api.watchlistInstrument(instrumentID, watchlistName),
                timeout=15,
            )
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            print(
                f"Cannot delete instrument. URL does not exist: {api.watchlistInstrument(instrumentID, watchlistName)}"
            )

        return response

    def deleteMultipleFromWatchlist(
        self, instrumentIds: List[str], watchlistName: str = None
    ):
        """
        Example Response Data:
        [<Response [204]>, <Response [204]>]
        """
        response = list(
            map(
                lambda instrumentId: self.deleteFromWatchlist(instrumentId),
                instrumentIds,
            )
        )

        return response

    @authRequired
    def reorderWatchList(
        self, instrumentIds: List[str], watchlistName: str = None
    ):
        """
        Example Response Data:
        {}
        """
        watchlistName = self._watchlistNameOrDefault(watchlistName)
        instrumentIdsField = ",".join(instrumentIds)
        payload = {"uuids": instrumentIdsField}

        response = self.session.post(
            api.watchlistReorder(), data=payload, timeout=15,
        )
        response.raise_for_status()

        data = response.json()

        return data

    def _watchlistNameOrDefault(self, watchlistName):
        allWatchlists = self.getAllWatchlists()

        if watchlistName is not None:
            if allWatchlists["next"]:
                nextUrl = allWatchlists["next"]
                watchlists = [allWatchlists["results"][0]]

                while nextUrl:
                    response = self.session.get(nextUrl, timeout=15)
                    response.raise_for_status()
                    data = response.json()
                    watchlist = data["results"][0]
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

