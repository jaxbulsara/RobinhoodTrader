from __future__ import absolute_import
from ..RobinhoodSession import RobinhoodSession
from ..endpoints import api
from ..wrappers import authRequired
from .PageSupport import PageSupport

import requests
from typing import List


class StockWatchlist(PageSupport):
    session: RobinhoodSession

    @authRequired
    def getFirstWatchlistPage(self) -> dict:
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
    def getWatchlist(self, watchlistName: str = "Default") -> List(dict):
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
        watchlistPage = self.getFirstWatchlistPage()
        watchlist = self.searchForRecord(watchlistPage, "name", watchlistName)
        if watchlist is None:
            watchlist = self.searchForRecord(watchlistPage, "name", "Default")
        response = self.session.get(watchlist.url, timeout=15)
        response.raise_for_status()
        data = response.json()["results"]

        return data

    def getWatchlistInstruments(self, watchlist: List[dict]) -> List[dict]:
        """
        Example Output:

        """
        instruments = []
        for instrument in watchlist:
            response = self.session.get(instrument.url, timeout=15)
            response.raise_for_status()
            data = response.json()
            instruments.append(data)

        return instruments

    @authRequired
    def addToWatchlist(self, instrument: dict, watchlist: List[dict]) -> dict:
        """
        Example Response Data:
        {   'created_at': '2020-02-16T22:56:18.685673Z',
            'instrument': 'https://api.robinhood.com/instruments/f4d089b7-c822-48ac-884d-8ecb312ebb67/',
            'url': 'https://api.robinhood.com/watchlists/Default/f4d089b7-c822-48ac-884d-8ecb312ebb67/',
            'watchlist': 'https://api.robinhood.com/watchlists/Default/'}
        """
        try:
            response = self.session.post(
                watchlist.url, data={"instrument": instrument.url}, timeout=15,
            )
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            print(
                f"Cannot add instrument. URL already exists: {watchlist.url + instrument.id + '/'}"
            )

        data = response.json()

        return data

    def addMultipleToWatchlist(
        self, instruments: List[dict], watchlist: List[dict]
    ) -> List[dict]:
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
        responses = list(
            map(
                lambda instrument: self.addToWatchlist(instrument, watchlist),
                instruments,
            )
        )

        return responses

    @authRequired
    def deleteFromWatchlist(
        self, instrument: dict, watchlist: List[dict],
    ) -> requests.Response:
        """
        Example Response Data:
        <Response [204]>
        """
        try:
            response = self.session.delete(
                watchlist.url + instrument.id + "/", timeout=15,
            )
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            print(
                f"Cannot delete instrument. URL does not exist: {watchlist.url + instrument.id + '/'}"
            )

        return response

    def deleteMultipleFromWatchlist(
        self, instruments: List[dict], watchlist: List[dict],
    ):
        """
        Example Response Data:
        [<Response [204]>, <Response [204]>]
        """
        response = list(
            map(
                lambda instrument: self.deleteFromWatchlist(
                    instrument, watchlist
                ),
                instruments,
            )
        )

        return response

    @authRequired
    def reorderWatchList(
        self, instruments: List[dict], watchlist: List[dict]
    ):
        """
        Example Response Data:
        {}
        """
        instrumentIds = list(map(lambda instrument: instrument.id, instruments))
        uuids = ",".join(instrumentIds)
        payload = {"uuids": uuids}

        response = self.session.post(
            api.watchlistReorder(), data=payload, timeout=15,
        )
        response.raise_for_status()
        data = response.json()

        return data

