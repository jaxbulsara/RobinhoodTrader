from __future__ import absolute_import

from ...RobinhoodTrader import RobinhoodSession
from ...wrappers import auth_required
from ...endpoints import nummus
from ...datatypes import Page, CryptoAccount
from ...exceptions import RecordNotFoundError, IdentifierError, CategoryError

from .Cryptocurrencies import Cryptocurrencies


class CryptoAccounts(Cryptocurrencies):
    session: RobinhoodSession

    def get_crypto_account(self, account_id=None):
        self.check_argument("account_id", account_id, str, type(None))

        if account_id:
            account = self._get_crypto_account_by_category(account_id)

        else:
            account = self._get_first_crypto_account()

        return CryptoAccount(account)

    def get_all_crypto_accounts(self):
        page = self._get_first_crypto_account_page()
        all_account_pages = self.get_pages(page)
        all_accounts = []

        for account_page in all_account_pages:
            for account in account_page.results:
                all_accounts.append(CryptoAccount(account))

        return all_accounts

    def _get_crypto_account_by_category(self, account_id):
        identifier_category = self.get_category("account_id", account_id)
        account_id_is_uuid = identifier_category == "uuid"

        if account_id_is_uuid:
            account = self._find_crypto_account_by_id(account_id)

        else:
            raise CategoryError(
                f"'account_id' must be a uuid, not {identifier_category}."
            )

        return account

    def _find_crypto_account_by_id(self, account_id):
        page = self._get_first_crypto_account_page()
        try:
            account = self.find_record(page, "id", account_id)

        except RecordNotFoundError:
            raise IdentifierError(
                f"Could not find crypto account with id '{account_id}'."
            )

        return account

    def _get_first_crypto_account(self):
        page = self._get_first_crypto_account_page()
        try:
            account = page.results[0]  # pylint: disable=no-member

        except IndexError:
            raise RecordNotFoundError(
                "Could not find a cryptocurrency account."
            )

        return account

    @auth_required
    def _get_first_crypto_account_page(self):
        endpoint = nummus.accounts()
        data = self.session.get_data(endpoint, timeout=15)
        return Page(data)

