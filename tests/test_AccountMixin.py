from RobinhoodTrader import RobinhoodTrader
from RobinhoodTrader.datatypes import (
    Account,
    AccountList,
    Page,
    InstantEligibility,
    MarginBalances,
)


def test_get_account(trader):
    trader: RobinhoodTrader

    account = trader.get_account()
    account = trader.get_account(account.account_number)

    expected_attributes = [
        "account_number",
        "active_subscription_id",
        "buying_power",
        "can_downgrade_to_cash",
        "cash",
        "cash_available_for_withdrawal",
        "cash_balances",
        "cash_held_for_orders",
        "cash_management_enabled",
        "created_at",
        "crypto_buying_power",
        "deactivated",
        "deposit_halted",
        "drip_enabled",
        "eligible_for_drip",
        "eligible_for_fractionals",
        "instant_eligibility",
        "is_pinnacle_account",
        "locked",
        "margin_balances",
        "max_ach_early_access_amount",
        "only_position_closing_trades",
        "option_level",
        "permanently_deactivated",
        "portfolio",
        "portfolio_cash",
        "positions",
        "received_ach_debit_locked",
        "rhs_account_number",
        "sma",
        "sma_held_for_orders",
        "state",
        "sweep_enabled",
        "type",
        "uncleared_deposits",
        "unsettled_debit",
        "unsettled_funds",
        "updated_at",
        "url",
        "user",
        "withdrawal_halted",
    ]

    assert type(account) == Account

    for attribute in expected_attributes:
        assert hasattr(account, attribute)


def test_get_account_instant_elibigility(trader):
    trader: RobinhoodTrader

    account = trader.get_account()

    expected_instant_eligibility_attributes = [
        "additional_deposit_needed",
        "compliance_user_major_oak_email",
        "created_at",
        "created_by",
        "reason",
        "reinstatement_date",
        "reversal",
        "state",
        "updated_at",
    ]

    if hasattr(account, "instant_eligibility"):
        assert type(account.instant_eligibility) == InstantEligibility

        for attribute in expected_instant_eligibility_attributes:
            assert hasattr(account.instant_eligibility, attribute)


def test_get_account_margin_balances(trader):
    trader: RobinhoodTrader

    account = trader.get_account()

    expected_margin_balances_attributes = [
        "cash",
        "cash_available_for_withdrawal",
        "cash_held_for_dividends",
        "cash_held_for_nummus_restrictions",
        "cash_held_for_options_collateral",
        "cash_held_for_orders",
        "cash_held_for_restrictions",
        "cash_pending_from_options_events",
        "created_at",
        "crypto_buying_power",
        "day_trade_buying_power",
        "day_trade_buying_power_held_for_orders",
        "day_trade_ratio",
        "day_trades_protection",
        "funding_hold_balance",
        "gold_equity_requirement",
        "margin_limit",
        "margin_withdrawal_limit",
        "marked_pattern_day_trader_date",
        "net_moving_cash",
        "outstanding_interest",
        "overnight_buying_power",
        "overnight_buying_power_held_for_orders",
        "overnight_ratio",
        "pending_debit_card_debits",
        "pending_deposit",
        "portfolio_cash",
        "settled_amount_borrowed",
        "sma",
        "start_of_day_dtbp",
        "start_of_day_overnight_buying_power",
        "unallocated_margin_cash",
        "uncleared_deposits",
        "uncleared_nummus_deposits",
        "unsettled_debit",
        "unsettled_funds",
        "updated_at",
    ]

    if hasattr(account, "margin_balances"):
        assert type(account.margin_balances) == MarginBalances

        for attribute in expected_margin_balances_attributes:
            assert hasattr(account.margin_balances, attribute)


def test__get_first_account_page(trader):
    trader: RobinhoodTrader

    page = trader._get_first_account_page()

    assert type(page) == Page
