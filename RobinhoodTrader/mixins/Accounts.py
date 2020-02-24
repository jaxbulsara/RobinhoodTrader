from __future__ import absolute_import
from ..RobinhoodSession import RobinhoodSession
from ..endpoints import api
from ..wrappers import authRequired
from .Instruments import Instruments
from typing import List, Optional


class Accounts(Instruments):
    session: RobinhoodSession

    @authRequired
    def getFirstAccountPage(self) -> dict:
        response = self.session.get(api.accounts(), timeout=15)
        response.raise_for_status()
        data = response.json()

        return data

    def getAllAccounts(self) -> List[dict]:
        page = self.getFirstAccountPage()
        allAccountPages = self.getPages(page)
        allAccounts = []
        for accountPage in allAccountPages:
            allAccounts.append(accountPage["results"])

        return allAccounts

    def getAccount(self, accountNumber: Optional[str] = None) -> dict:
        page = self.getFirstAccountPage()
        if accountNumber is not None:
            account = self.searchForRecord(
                page, "account_number", accountNumber
            )
        else:
            account = page["results"][0]

        return account

    @authRequired
    def getPositions(self) -> dict:
        response = self.session.get(api.positions(), timeout=15)
        response.raise_for_status()
        data = response.json()

        return data
