from .Broker import Broker
from RobinhoodTrader import endpoints
from RobinhoodTrader.session import RobinhoodSession
from RobinhoodTrader.session.wrappers import authRequired


class StockBroker(Broker):
    @authRequired
    def getWatchlists(self, session: RobinhoodSession):
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
