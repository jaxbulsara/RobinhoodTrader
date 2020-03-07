from RobinhoodTrader import RobinhoodTrader
from RobinhoodTrader.datatypes import Page


def test__pages(trader):
    trader: RobinhoodTrader

    page = trader._get_first_account_page()
    pages = trader.get_pages(page)

    assert type(page) == Page
    assert type(pages) == list

