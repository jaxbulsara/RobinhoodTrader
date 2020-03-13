from __future__ import absolute_import

api = "https://api.robinhood.com/"


def accounts():
    return api + "accounts/"


def account_by_number(accountNumber):
    return accounts() + accountNumber + "/"


def account_portfolio(accountNumber):
    return account_by_number(accountNumber) + "/portfolio/"


def account_positions(accountNumber):
    return account_by_number(accountNumber) + "/positions/"


def forex_quotes():
    return api + "marketdata/forex/quotes/{}"


def forex_historicals(symbol, interval=None, span=None, bounds=None):
    endpoint = api + f"marketdata/forex/historicals/{symbol}/"
    if interval:
        endpoint += f"?interval={interval}"
    if span:
        endpoint += f"?span={span}"
    if bounds:
        endpoint += f"?bounds={bounds}"

    return endpoint


def fundamentals():
    return api + "fundamentals/"


def fundamentals_by_symbol(symbol):
    return fundamentals() + symbol + "/"


def historicals():
    return api + "quotes/historicals"


def instruments():
    return api + "instruments/"


def instrument_by_symbol(symbol):
    return instruments() + "?symbol=" + symbol


def instrument_by_id(instrumentId):
    return instruments() + instrumentId + "/"


def markets():
    return api + "markets/"


def market_by_mic(identifier_code):
    return markets() + identifier_code + "/"


def market_hours_by_date(identifier_code, dateString):
    return markets() + identifier_code + "/hours/" + dateString + "/"


def midlands():
    return api + "midlands/"


def midlands_lists():
    return midlands() + "lists/"


def midland_list_by_id(list_id):
    return midlands_lists() + list_id + "/"


def midlands_lists_items():
    return midlands_lists() + "items/"


def options():
    return api + "options/"


def option_positions():
    return api + "options/positions/"


def option_orders():
    return api + "options/orders"


def option_instruments():
    return api + "options/instruments/"


def orders():
    return api + "orders/"


def portfolios():
    return api + "portfolios/"


def positions():
    return api + "positions/"


def quotes():
    return api + "quotes/"


def quote_by_symbol(symbol: str):
    return quotes() + symbol + "/"


def tags():
    return api + "midland/tags/tag/"


def token():
    return api + "/oauth2/token/"


def revoke_token():
    return api + "/oauth2/revoke_token/"


def user():
    return api + "user/"


def user_additional_info():
    return api + "user/additional_info/"


def user_basic_info():
    return api + "user/basic_info/"


def user_cip_questions():
    return api + "user/cip_questions/"


def user_employment():
    return api + "user/employment/"


def user_identity_mismatch():
    return api + "user/identity_mismatch/"


def user_investment_profile():
    return api + "user/investment_profile/"


def watchlists():
    return api + f"watchlists/"


def watchlist_by_name(name: str = None):
    if name is None:
        name = "Default"
    return api + f"watchlists/{name}/"


def watchlist_instrument(instrument_id: str, name: str = None):
    return watchlist_by_name(name) + f"{instrument_id}/"


def watchlist_reorder(name: str = None):
    return watchlist_by_name(name) + "reorder/"

