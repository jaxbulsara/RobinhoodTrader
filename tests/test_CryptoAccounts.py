from RobinhoodTrader import RobinhoodTrader
from RobinhoodTrader.exceptions import (
    IdentifierError,
    CategoryError,
    RecordNotFoundError,
)
from RobinhoodTrader.datatypes import Page, CryptoAccount

from uuid import uuid4
import pytest


def test_get_crypto_account(trader):
    trader: RobinhoodTrader

    account = trader.get_crypto_account()

    expected_attributes = [
        "created_at",
        "id",
        "status",
        "status_reason_code",
        "updated_at",
        "user_id",
    ]

    assert type(account) == CryptoAccount

    for attribute in expected_attributes:
        assert hasattr(account, attribute)


def test_get_crypto_account_bad_category(trader):
    trader: RobinhoodTrader

    with pytest.raises(CategoryError):
        trader.get_crypto_account("ABCD")


def test_get_crypto_account_bad_identifier(trader):
    trader: RobinhoodTrader

    with pytest.raises(IdentifierError):
        trader.get_crypto_account(str(uuid4()))


def test_get_crypto_account_no_accounts_in_page(trader, monkeypatch):
    trader: RobinhoodTrader

    def page_with_no_results():
        page_with_no_results = Page(
            {"previous": None, "next": None, "results": [],}
        )
        return page_with_no_results

    monkeypatch.setattr(
        trader, "_get_first_crypto_account_page", page_with_no_results
    )

    with pytest.raises(RecordNotFoundError):
        trader.get_crypto_account()


def test_get_all_crypto_accounts(trader):
    trader: RobinhoodTrader

    all_accounts = trader.get_all_crypto_accounts()

    assert type(all_accounts) == list

    for account in all_accounts:
        assert type(account) == CryptoAccount


def test__get_first_crypto_account_page(trader):
    trader: RobinhoodTrader

    first_crypto_page = trader._get_first_crypto_account_page()

    assert type(first_crypto_page) == Page
