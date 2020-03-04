from __future__ import absolute_import
from ..RobinhoodSession import RobinhoodSession
from ..endpoints import api
from ..wrappers import authRequired
from ..exceptions import SymbolError
from .Instruments import Instruments
from typing import List, Optional


class Accounts(Instruments):
    session: RobinhoodSession

    @authRequired
    def getFirstAccountPage(self) -> dict:
        endpoint = api.accounts()
        return self.session.getData(endpoint, timeout=15)

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
            try:
                account = page["results"][0]
            except IndexError:
                raise SymbolError(
                    f"Could not find account with number {accountNumber}."
                )

        return account

    @authRequired
    def getPositions(self) -> dict:
        endpoint = api.positions()
        return self.session.getData(endpoint, timeout=15)
