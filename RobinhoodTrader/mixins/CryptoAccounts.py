from __future__ import absolute_import
from ..RobinhoodSession import RobinhoodSession
from ..endpoints import nummus
from ..wrappers import authRequired
from .Cryptocurrencies import Cryptocurrencies
from typing import Optional, List


class CryptoAccounts(Cryptocurrencies):
    session: RobinhoodSession

    def getFirstCryptoAccountPage(self) -> dict:
        endpoint = nummus.accounts()
        return self.session.getData(endpoint, timeout=15)

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
            try:
                account = page["results"][0]
            except IndexError:
                account = None

        return account

    @authRequired
    def getCryptoHoldings(self) -> dict:
        endpoint = nummus.holdings()
        return self.session.getData(endpoint, timeout=15)

