from __future__ import absolute_import
from ..RobinhoodSession import RobinhoodSession
from ..endpoints import api
from ..wrappers import authRequired
from .PageSupport import PageSupport

import requests
from typing import List, Optional


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
    def getWatchlist(self, watchlistName: str = "Default") -> dict:
        """
        Example response:
        {   'name': 'Default',
            'next': None,
            'previous': None,
            'results': [   {   'created_at': '2020-02-17T00:31:27.748087Z',
                            'instrument': 'https://api.robinhood.com/instruments/50810c35-d215-4866-9758-0ada4ac79ffa/',
                            'url': 'https://api.robinhood.com/watchlists/Default/50810c35-d215-4866-9758-0ada4ac79ffa/',
                            'watchlist': 'https://api.robinhood.com/watchlists/Default/'},
                        {   'created_at': '2020-02-16T23:24:48.569037Z',
                            'instrument': 'https://api.robinhood.com/instruments/450dfc6d-5510-4d40-abfb-f633b7d9be3e/',
                            'url': 'https://api.robinhood.com/watchlists/Default/450dfc6d-5510-4d40-abfb-f633b7d9be3e/',
                            'watchlist': 'https://api.robinhood.com/watchlists/Default/'},
                        {   'created_at': '2020-02-17T01:12:58.590500Z',
                            'instrument': 'https://api.robinhood.com/instruments/e39ed23a-7bd1-4587-b060-71988d9ef483/',
                            'url': 'https://api.robinhood.com/watchlists/Default/e39ed23a-7bd1-4587-b060-71988d9ef483/',
                            'watchlist': 'https://api.robinhood.com/watchlists/Default/'},
                        {   'created_at': '2020-02-17T01:12:58.736878Z',
                            'instrument': 'https://api.robinhood.com/instruments/54db869e-f7d5-45fb-88f1-8d7072d4c8b2/',
                            'url': 'https://api.robinhood.com/watchlists/Default/54db869e-f7d5-45fb-88f1-8d7072d4c8b2/',
                            'watchlist': 'https://api.robinhood.com/watchlists/Default/'}],
            'url': 'https://api.robinhood.com/watchlists/Default/',
            'user': 'api.robinhood.com/user/'}
            ]
        """
        watchlistPage = self.getFirstWatchlistPage()
        watchlist = self.searchForRecord(watchlistPage, "name", watchlistName)
        if watchlist is None:
            watchlist = self.searchForRecord(watchlistPage, "name", "Default")
        response = self.session.get(watchlist["url"], timeout=15)
        response.raise_for_status()
        data = response.json()
        data["name"] = watchlist["name"]
        data["url"] = watchlist["url"]
        data["user"] = watchlist["user"]

        return data


    @authRequired
    def getWatchlistInstruments(self, watchlist: Optional[List[dict]] = None) -> List[dict]:
        """
        Example Output
        [   {   'bloomberg_unique': 'EQ0010174300001000',
                'country': 'US',
                'day_trade_ratio': '0.2500',
                'default_collar_fraction': '0.05',
                'fractional_tradability': 'tradable',
                'fundamentals': 'https://api.robinhood.com/fundamentals/MSFT/',
                'id': '50810c35-d215-4866-9758-0ada4ac79ffa',
                'list_date': '1987-09-17',
                'maintenance_ratio': '0.2500',
                'margin_initial_ratio': '0.5000',
                'market': 'https://api.robinhood.com/markets/XNAS/',
                'min_tick_size': None,
                'name': 'Microsoft Corporation Common Stock',
                'quote': 'https://api.robinhood.com/quotes/MSFT/',
                'rhs_tradability': 'tradable',
                'simple_name': 'Microsoft',
                'splits': 'https://api.robinhood.com/instruments/50810c35-d215-4866-9758-0ada4ac79ffa/splits/',
                'state': 'active',
                'symbol': 'MSFT',
                'tradability': 'tradable',
                'tradable_chain_id': '1ac71e01-0677-42c6-a490-1457980954f8',
                'tradeable': True,
                'type': 'stock',
                'url': 'https://api.robinhood.com/instruments/50810c35-d215-4866-9758-0ada4ac79ffa/'},
            ...
            ...
            ...
            {   'bloomberg_unique': 'EQ0000000044666717',
                'country': 'US',
                'day_trade_ratio': '0.2500',
                'default_collar_fraction': '0.05',
                'fractional_tradability': 'tradable',
                'fundamentals': 'https://api.robinhood.com/fundamentals/GOOGL/',
                'id': '54db869e-f7d5-45fb-88f1-8d7072d4c8b2',
                'list_date': '2004-08-19',
                'maintenance_ratio': '0.2500',
                'margin_initial_ratio': '0.5000',
                'market': 'https://api.robinhood.com/markets/XNAS/',
                'min_tick_size': None,
                'name': 'Alphabet Inc. Class A Common Stock',
                'quote': 'https://api.robinhood.com/quotes/GOOGL/',
                'rhs_tradability': 'tradable',
                'simple_name': 'Alphabet Class A',
                'splits': 'https://api.robinhood.com/instruments/54db869e-f7d5-45fb-88f1-8d7072d4c8b2/splits/',
                'state': 'active',
                'symbol': 'GOOGL',
                'tradability': 'tradable',
                'tradable_chain_id': '9f75b6b7-ef7e-4942-99b9-be7d81db8e6e',
                'tradeable': True,
                'type': 'stock',
                'url': 'https://api.robinhood.com/instruments/54db869e-f7d5-45fb-88f1-8d7072d4c8b2/'}]
        """
        if watchlist is None:
            watchlist = self.getWatchlist()
        instruments = []
        for instrument in watchlist["results"]:
            response = self.session.get(instrument["instrument"], timeout=15)
            response.raise_for_status()
            data = response.json()
            instruments.append(data)

        return instruments

    @authRequired
    def addToWatchlist(self, instrument: dict, watchlist: Optional[List[dict]] = None) -> dict:
        """
        Example Response Data:
        {   'created_at': '2020-02-16T22:56:18.685673Z',
            'instrument': 'https://api.robinhood.com/instruments/f4d089b7-c822-48ac-884d-8ecb312ebb67/',
            'url': 'https://api.robinhood.com/watchlists/Default/f4d089b7-c822-48ac-884d-8ecb312ebb67/',
            'watchlist': 'https://api.robinhood.com/watchlists/Default/'}
        """
        if watchlist is None:
            watchlist = self.getWatchlist()
        try:
            response = self.session.post(
                watchlist["url"], data={"instrument": instrument["url"]}, timeout=15,
            )
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            print(
                f"Cannot add instrument. URL already exists: {watchlist['url'] + instrument['id'] + '/'}"
            )

        data = response.json()

        return data

    def addMultipleToWatchlist(
        self, instruments: List[dict], watchlist: Optional[List[dict]] = None
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
        if watchlist is None:
            watchlist = self.getWatchlist()
        responses = list(
            map(
                lambda instrument: self.addToWatchlist(instrument, watchlist),
                instruments,
            )
        )

        return responses

    @authRequired
    def deleteFromWatchlist(
        self, instrument: dict, watchlist: Optional[List[dict]] = None
    ) -> requests.Response:
        """
        Example Response Data:
        <Response [204]>
        """
        if watchlist is None:
            watchlist = self.getWatchlist()
        try:
            response = self.session.delete(
                watchlist["url"] + instrument["id"] + "/", timeout=15,
            )
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            print(
                f"Cannot delete instrument. URL does not exist: {watchlist['url'] + instrument['id'] + '/'}"
            )

        return response

    def deleteMultipleFromWatchlist(
        self, instruments: List[dict], watchlist: Optional[List[dict]] = None,
    ):
        """
        Example Response Data:
        [<Response [204]>, <Response [204]>]
        """
        if watchlist is None:
            watchlist = self.getWatchlist()
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
    def reorderWatchList(self, instruments: List[dict], watchlist: Optional[List[dict]] = None):
        """
        Example Response Data:
        {}
        """
        if watchlist is None:
            watchlist = self.getWatchlist()
        instrumentIds = list(map(lambda instrument: instrument["id"], instruments))
        uuids = ",".join(instrumentIds)
        payload = {"uuids": uuids}

        response = self.session.post(
            api.watchlistReorder(), data=payload, timeout=15,
        )
        response.raise_for_status()
        data = response.json()

        return data

