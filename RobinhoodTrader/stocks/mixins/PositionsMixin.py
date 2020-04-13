from __future__ import absolute_import

from ...session import RobinhoodSession
from ...wrappers import auth_required
from ...endpoints import api
from ...datatypes import Positions, Position

from .InstrumentMixin import InstrumentMixin


class PositionsMixin(InstrumentMixin):
    session: RobinhoodSession

    @auth_required
    def get_positions(self):
        endpoint = api.positions()
        data = self.session.get_data(endpoint, timeout=15)

        raw_positions = data["results"]
        positions = Positions()

        for raw_position in raw_positions:
            raw_position.update(
                {
                    "trader": self,
                    "account_url": raw_position["account"],
                    "instrument_url": raw_position["instrument"],
                }
            )

            raw_position.pop("account")
            raw_position.pop("instrument")

            position = Position(raw_position)
            positions.append(position)

        return positions
