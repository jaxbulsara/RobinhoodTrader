from __future__ import absolute_import
from ..RobinhoodSession import RobinhoodSession
from ..endpoints import api
from ..wrappers import authRequired
from .Instruments import Instruments

import requests
from typing import List, Optional


class InstrumentWatchlists(Instruments):
    session: RobinhoodSession

    @authRequired
    def getFirstWatchlistPage(self) -> dict:
        endpoint = api.watchlists()
        return self.session.getData(endpoint, timeout=15)

    @authRequired
    def getWatchlist(self, watchlistName: str = "Default") -> dict:
        watchlistPage = self.getFirstWatchlistPage()
        watchlist = self.searchForRecord(watchlistPage, "name", watchlistName)
        if watchlist is None:
            watchlist = self.searchForRecord(watchlistPage, "name", "Default")

        endpoint = watchlist["url"]
        data = self.session.getData(endpoint, timeout=15)

        data["name"] = watchlist["name"]
        data["url"] = watchlist["url"]
        data["user"] = watchlist["user"]

        return data

    @authRequired
    def getWatchlistInstruments(
        self, watchlist: Optional[dict] = None
    ) -> List[dict]:
        if watchlist is None:
            watchlist = self.getWatchlist()
        instruments = []
        for instrument in watchlist["results"]:
            endpoint = instrument["instrument"]
            data = self.session.getData(endpoint, timeout=15)
            instruments.append(data)

        return instruments

    @authRequired
    def addToWatchlist(
        self, instrument: dict, watchlist: Optional[dict] = None
    ) -> dict:
        if watchlist is None:
            watchlist = self.getWatchlist()
        try:
            response = self.session.post(
                watchlist["url"],
                data={"instrument": instrument["url"]},
                timeout=15,
            )
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            print(
                f"Cannot add instrument. URL already exists: {watchlist['url'] + instrument['id'] + '/'}"
            )

        data = response.json()

        return data

    def addMultipleToWatchlist(
        self, instruments: List[dict], watchlist: Optional[dict] = None
    ) -> List[dict]:
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
        self, instrument: dict, watchlist: Optional[dict] = None
    ) -> requests.Response:
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
        self, instruments: List[dict], watchlist: Optional[dict] = None,
    ):
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
    def reorderWatchList(
        self,
        reorderedInstruments: List[dict],
        watchlist: Optional[dict] = None,
    ):
        if watchlist is None:
            watchlist = self.getWatchlist()
        reorderedInstrumentIds = list(
            map(lambda instrument: instrument["id"], reorderedInstruments)
        )
        reorderedUuids = ",".join(reorderedInstrumentIds)
        payload = {"uuids": reorderedUuids}

        endpoint = api.watchlistReorder()
        return self.session.postData(endpoint, data=payload, timeout=15,)

