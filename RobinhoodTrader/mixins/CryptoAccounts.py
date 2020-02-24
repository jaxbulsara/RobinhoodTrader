from __future__ import absolute_import
from ..RobinhoodSession import RobinhoodSession
from ..endpoints import nummus
from ..wrappers import authRequired
from .Cryptocurrencies import Cryptocurrencies
from typing import Optional, List


class CryptoAccounts(Cryptocurrencies):
    session: RobinhoodSession

    def getFirstCryptoAccountPage(self) -> dict:
        response = self.session.get(nummus.accounts(), timeout=15)
        response.raise_for_status()
        data = response.json()

        return data

    def getAllCryptoAccounts(self) -> List[dict]:
        page = self.getFirstCryptoAccountPage()
        allAccountPages = self.getPages(page)
        allAccounts = []
        for accountPage in allAccountPages:
            allAccounts.append(accountPage["results"])

        return allAccounts

    def getCryptoAccount(self, accountId: Optional[str] = None) -> dict:
        page = self.getFirstCryptoAccountPage()
        if accountId is not None:
            account = self.searchForRecord(page, "id", accountId)
        else:
            account = page["results"][0]

        return account

    @authRequired
    def getCryptoHoldings(self) -> dict:
        response = self.session.get(nummus.holdings(), timeout=15)
        response.raise_for_status()
        data = response.json()

        return data

