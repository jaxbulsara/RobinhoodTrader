from __future__ import absolute_import

from ...RobinhoodSession import RobinhoodSession
from ...wrappers import auth_required
from ...endpoints import api

from .Instruments import Instruments

import requests


class InstrumentWatchlists(Instruments):
    session: RobinhoodSession

    @auth_required
    def get_watchlist(self, watchlist_name="Default"):
        page = self._get_first_watchlist_page()
        watchlist = self.find_record(page, "name", watchlist_name)
        if watchlist is None:
            watchlist = self.find_record(page, "name", "Default")

        endpoint = watchlist["url"]
        data = self.session.get_data(endpoint, timeout=15)

        metadata = {
            "name": watchlist["name"],
            "url": watchlist["url"],
            "user": watchlist["user"],
        }
        data.update(metadata)

        return data

    @auth_required
    def get_watchlist_instruments(self, watchlist=None):
        if watchlist is None:
            watchlist = self.get_watchlist()

        instruments = []
        for instrument in watchlist["results"]:
            endpoint = instrument["instrument"]
            data = self.session.get_data(endpoint, timeout=15)
            instruments.append(data)

        return instruments

    @auth_required
    def add_to_watchlist(self, instrument, watchlist=None):
        if watchlist is None:
            watchlist = self.get_watchlist()

        try:
            data = self.session.post_data(
                watchlist["url"],
                data={"instrument": instrument["url"]},
                timeout=15,
            )
        except requests.exceptions.HTTPError:
            print(
                f"Cannot add instrument. URL already exists: {watchlist['url'] + instrument['id'] + '/'}"
            )

        return data

    def add_multiple_to_watchlist(self, instruments, watchlist=None):
        if watchlist is None:
            watchlist = self.get_watchlist()

        responses = list(
            map(
                lambda instrument: self.add_to_watchlist(instrument, watchlist),
                instruments,
            )
        )

        return responses

    @auth_required
    def delete_from_watchlist(self, instrument, watchlist=None):
        if watchlist is None:
            watchlist = self.get_watchlist()

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

    def delete_multiple_from_watchlist(
        self, instruments, watchlist=None,
    ):
        if watchlist is None:
            watchlist = self.get_watchlist()

        response = list(
            map(
                lambda instrument: self.delete_from_watchlist(
                    instrument, watchlist
                ),
                instruments,
            )
        )

        return response

    @auth_required
    def reorder_watchlist(
        self, reordered_instruments, watchlist=None,
    ):
        if watchlist is None:
            watchlist = self.get_watchlist()

        reordered_instrument_ids = list(
            map(lambda instrument: instrument["id"], reordered_instruments)
        )
        reordered_uuids = ",".join(reordered_instrument_ids)
        payload = {"uuids": reordered_uuids}

        endpoint = api.watchlist_reorder()
        return self.session.post_data(endpoint, data=payload, timeout=15,)

    @auth_required
    def _get_first_watchlist_page(self) -> dict:
        endpoint = api.watchlists()
        return self.session.get_data(endpoint, timeout=15)

