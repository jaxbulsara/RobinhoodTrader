from __future__ import absolute_import

from ...RobinhoodSession import RobinhoodSession
from ...wrappers import auth_required
from ...endpoints import api
from ...exceptions import RecordNotFoundError, IdentifierError
from ...datatypes import Page

from .Instruments import Instruments


class Accounts(Instruments):
    session: RobinhoodSession

    def get_account(self, account_number=None):
        if account_number:
            account = self._get_account_by_number(account_number)
        else:
            page = self._get_first_account_page()
            account = page["results"][0]

        return account

    def get_all_accounts(self):
        page = self._get_first_account_page()
        all_account_pages = self.get_pages(page)
        all_accounts = []
        for accountPage in all_account_pages:
            all_accounts.append(accountPage["results"])

        return all_accounts

    def _get_account_by_number(self, account_number):
        page = self._get_first_account_page()
        try:
            account = self.find_record(page, "account_number", account_number)
        except RecordNotFoundError:
            raise IdentifierError(
                f"Could not find account with number '{account_number}'."
            )

        return account

    @auth_required
    def _get_first_account_page(self):
        endpoint = api.accounts()
        data = self.session.get_data(endpoint, timeout=15)
        return Page(data)
