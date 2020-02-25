from __future__ import absolute_import
from ..RobinhoodSession import RobinhoodSession
from ..endpoints import api
from ..wrappers import authRequired
import datetime


class Markets:
    session: RobinhoodSession

    @authRequired
    def getFirstMarketPage(self) -> dict:
        endpoint = api.markets()
        return self.session.getData(endpoint, timeout=15)

    @authRequired
    def getMarketByIdentifierCode(self, identifierCode: str) -> dict:
        endpoint = api.marketByIdentifierCode(identifierCode)
        return self.session.getData(endpoint, timeout=15)

    @authRequired
    def getMarketByInstrument(self, instrument: dict) -> dict:
        endpoint = instrument["market"]
        return self.session.getData(endpoint, timeout=15)

    @authRequired
    def getMarketHours(self, market: dict):
        endpoint = market["todays_hours"]
        return self.session.getData(endpoint, timeout=15)

    @authRequired
    def getMarketNextDayHours(self, market: dict):
        marketHours = self.getMarketHours(market)
        endpoint = marketHours["next_open_hours"]
        
        return self.session.getData(endpoint, timeout=15)

    @authRequired
    def getMarketHoursByDate(self, market: dict, date: datetime.date):
        dateString = date.strftime("%Y-%m-%d")
        endpoint = api.marketHoursByDate(market["mic"], dateString)

        return self.session.getData(endpoint, timeout=15)
