from RobinhoodTrader import RobinhoodTrader
from RobinhoodTrader.datatypes import (
    CryptoHoldings,
    CryptoHolding,
    CostBases,
    CostBasis,
    Currency,
)


def test_get_crypto_holdings(trader):
    trader: RobinhoodTrader

    crypto_holdings = trader.get_crypto_holdings()

    expected_attributes = [
        "account_id",
        "cost_bases",
        "created_at",
        "currency",
        "id",
        "quantity",
        "quantity_available",
        "quantity_held_for_buy",
        "quantity_held_for_sell",
        "updated_at",
    ]

    assert type(crypto_holdings) == CryptoHoldings
    for holding in crypto_holdings:
        assert type(holding) == CryptoHolding

        for attribute in expected_attributes:
            assert hasattr(holding, attribute)


def test_get_crypto_holdings_currency(trader):
    trader: RobinhoodTrader

    crypto_holdings = trader.get_crypto_holdings()

    expected_currency_keys = [
        "brand_color",
        "code",
        "id",
        "increment",
        "name",
        "type",
    ]

    for holding in crypto_holdings:
        assert type(holding.currency) == Currency

        for attribute in expected_currency_keys:
            assert hasattr(holding.currency, attribute)


def test_get_crypto_holdings_cost_bases(trader):
    trader: RobinhoodTrader

    crypto_holdings = trader.get_crypto_holdings()

    expected_cost_basis_attributes = [
        "currency_id",
        "direct_cost_basis",
        "direct_quantity",
        "id",
        "intraday_cost_basis",
        "intraday_quantity",
        "marked_cost_basis",
        "marked_quantity",
    ]

    for holding in crypto_holdings:
        assert type(holding.cost_bases) == CostBases
        for cost_basis in holding.cost_bases:
            assert type(cost_basis) == CostBasis

            for attribute in expected_cost_basis_attributes:
                assert hasattr(cost_basis, attribute)
