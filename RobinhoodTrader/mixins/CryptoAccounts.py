from __future__ import absolute_import
from ..RobinhoodSession import RobinhoodSession
from ..endpoints import nummus
from ..wrappers import auth_required
from .Cryptocurrencies import Cryptocurrencies


class CryptoAccounts(Cryptocurrencies):
    session: RobinhoodSession

    def get_crypto_account(self, accountId=None):
        page = self._get_first_crypto_account_page()
        if accountId is not None:
            account = self.find_record(page, "id", accountId)
        else:
            try:
                account = page["results"][0]
            except IndexError:
                account = None

        return account

    def get_all_crypto_accounts(self):
        page = self._get_first_crypto_account_page()
        allAccountPages = self.get_pages(page)
        allAccounts = []
        for accountPage in allAccountPages:
            allAccounts.append(accountPage["results"])

        return allAccounts

    def _get_first_crypto_account_page(self):
        endpoint = nummus.accounts()
        return self.session.get_data(endpoint, timeout=15)

