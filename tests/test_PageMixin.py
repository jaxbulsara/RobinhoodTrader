from RobinhoodTrader import RobinhoodTrader
from RobinhoodTrader.datatypes import Page
from RobinhoodTrader.exceptions import PageError, RecordNotFoundError
import requests, pytest


def test_Page(trader):
    trader: RobinhoodTrader

    page = trader._get_first_instrument_page()

    expected_attributes = ["previous", "next", "results"]

    assert type(page) == Page

    for attribute in expected_attributes:
        assert hasattr(page, attribute)


def test_get_pages(trader):
    trader: RobinhoodTrader

    page = trader._get_first_instrument_page()
    pages = trader.get_pages(page, limit=2)

    assert type(pages) == list

    for page in pages:
        assert type(page) == Page


def test_find_record(trader):
    trader: RobinhoodTrader

    page = trader._get_first_account_page()

    with pytest.raises(RecordNotFoundError):
        trader.find_record(page, "user", "wrong_url")

    record = trader.find_record(page, "user", "api.robinhood.com/user/")

    assert type(record) == dict


def test_next_page_exists(trader):
    trader: RobinhoodTrader

    instrument_page = trader._get_first_instrument_page()
    account_page = trader._get_first_account_page()

    assert instrument_page.next is not None
    assert account_page.next is None


def test_get_next_page(trader):
    trader: RobinhoodTrader

    page = trader._get_first_instrument_page()
    next_page = trader.get_next_page(page)

    assert type(next_page) == Page

    page = trader._get_first_account_page()
    with pytest.raises(PageError):
        next_page = trader.get_next_page(page)

