from RobinhoodTrader import RobinhoodTrader
from RobinhoodTrader.datatypes import Page
from RobinhoodTrader.exceptions import PageError
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

    page = trader._get_first_watchlist_page()
    record = trader.find_record(page, "name", "Default")

    assert type(record) == dict


def test_next_page_exists(trader):
    trader: RobinhoodTrader

    instrument_page = trader._get_first_instrument_page()
    watchlist_page = trader._get_first_watchlist_page()

    assert instrument_page.next is not None
    assert watchlist_page.next is None


def test_get_next_page(trader):
    trader: RobinhoodTrader

    page = trader._get_first_instrument_page()
    next_page = trader.get_next_page(page)

    assert type(next_page) == Page

    page = trader._get_first_watchlist_page()
    with pytest.raises(PageError):
        next_page = trader.get_next_page(page)

