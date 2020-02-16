from .Broker import Broker
from RobinhoodTrader import endpoints
from RobinhoodTrader.session import RobinhoodSession
from RobinhoodTrader.session.wrappers import authRequired


class StockBroker(Broker):
    @authRequired
    def getAllWatchlists(self, session: RobinhoodSession):
        """
        Example response:
        {   'next': None,
            'previous': None,
            'results': [   {   'name': 'Default',
                            'url': 'https://api.robinhood.com/watchlists/Default/',
                            'user': 'api.robinhood.com/user/'}]} 
        """

        response = session.get(endpoints.watchlist(), timeout=15)
        response.raise_for_status()
        data = response.json()

        return data

    @authRequired
    def getWatchlist(self, session: RobinhoodSession, watchlistName: str):
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

        response = session.get(endpoints.watchlist(watchlistName), timeout=15)
        response.raise_for_status()
        data = response.json()["results"]

        return data
