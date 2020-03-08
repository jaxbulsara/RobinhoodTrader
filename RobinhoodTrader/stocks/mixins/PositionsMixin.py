from __future__ import absolute_import

from ...session import RobinhoodSession
from ...wrappers import auth_required
from ...endpoints import api

from .InstrumentMixin import InstrumentMixin


class PositionsMixin(InstrumentMixin):
    session: RobinhoodSession

    @auth_required
    def get_positions(self) -> dict:
        endpoint = api.positions()
        return self.session.get_data(endpoint, timeout=15)
