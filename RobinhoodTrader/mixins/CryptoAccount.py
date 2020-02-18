from __future__ import absolute_import
from ..RobinhoodSession import RobinhoodSession
from ..endpoints import nummus
from ..wrappers import authRequired


class CryptoAccount:
    session: RobinhoodSession

    @authRequired
    def getAllCryptoAccounts(self):
        """
        Example Response Data:
        {   'next': None,
            'previous': None,
            'results': [   {'created_at': '2019-01-022T19:27:18.126854-04:00',
                            'id': '33129d88-2c61-404a-b802-71d2714cfc1a',
                            'status': 'active',
                            'status_reason_code': '',
                            'updated_at': '2019-01-022T19:27:18.126854-04:00',
                            'user_id': '0573f88e-6741-415e-a64c-0442fa90deb7'}]}
        """
        response = self.session.get(nummus.accounts(), timeout=15)
        response.raise_for_status()
        data = response.json()

        return data

    def getCryptoAccount(self, accountId: str = None):
        """
        Example Response Data:
        {   'created_at': '2019-01-022T19:27:18.126854-04:00',
            'id': '33129d88-2c61-404a-b802-71d2714cfc1a',
            'status': 'active',
            'status_reason_code': '',
            'updated_at': '2019-01-022T19:27:18.126854-04:00',
            'user_id': '0573f88e-6741-415e-a64c-0442fa90deb7'}
        """
        accountId = self._getAccountIdOrDefault(accountId)
        response = self.session.get(nummus.accountById(accountId), timeout=15)
        response.raise_for_status()
        data = response.json()

        return data

    def _getAccountIdOrDefault(self, accountId: str = None):
        allAccounts = self.getAllCryptoAccounts()
        accounts = [allAccounts["results"][0]]
        firstAccountId = accounts[0]["id"]

        if accountId is not None:
            if allAccounts["next"]:
                nextUrl = allAccounts["next"]

                while nextUrl:
                    response = self.session.get(nextUrl, timeout=15)
                    response.raise_for_status()
                    data = response.json()
                    account = data["results"]
                    accounts.append(account)

                for account in accounts:
                    if accountId not in account["id"]:
                        accountId = firstAccountId

            else:
                for account in accounts:
                    if accountId not in account["id"]:
                        accountId = firstAccountId
        else:
            accountId = firstAccountId

        return accountId
