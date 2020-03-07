from __future__ import absolute_import
from ..RobinhoodSession import RobinhoodSession
from ..endpoints import api
from ..wrappers import auth_required
from .Instruments import Instruments


class Positions(Instruments):
    session: RobinhoodSession

    @auth_required
    def get_positions(self) -> dict:
        endpoint = api.positions()
        return self.session.get_data(endpoint, timeout=15)
