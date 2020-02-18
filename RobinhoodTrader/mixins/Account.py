from __future__ import absolute_import
from ..RobinhoodSession import RobinhoodSession
from ..endpoints import api
from ..wrappers import authRequired


class Account:
    session: RobinhoodSession

    def getAllAccounts(self):
        """
        Example Response Data:
        {   'next': None,
            'previous': None,
            'results': [   {   'account_number': '8TV36483',
                            'active_subscription_id': '72d1b8ab-5e00-4472-bef3-6b3437d3bae1',
                            'buying_power': '314.1500',
                            'can_downgrade_to_cash': 'https://api.robinhood.com/accounts/5QT19448/can_downgrade_to_cash/',
                            'cash': '561.3400',
                            'cash_available_for_withdrawal': '314.1500',
                            'cash_balances': None,
                            'cash_held_for_orders': '0.0000',
                            'cash_management_enabled': False,
                            'created_at': '2017-03-11T18:12:13.256678Z',
                            'crypto_buying_power': '314.1500',
                            'deactivated': False,
                            'deposit_halted': False,
                            'drip_enabled': False,
                            'eligible_for_drip': False,
                            'eligible_for_fractionals': False,
                            'instant_eligibility': {   'additional_deposit_needed': '0.0000',
                                                        'compliance_user_major_oak_email': None,
                                                        'created_at': '2017-03-11T18:12:13.256678Z',
                                                        'created_by': None,
                                                        'reason': '',
                                                        'reinstatement_date': None,
                                                        'reversal': None,
                                                        'state': 'ok',
                                                        'updated_at': None},
                            'is_pinnacle_account': True,
                            'locked': False,
                            'margin_balances': {   'cash': '561.3400',
                                                    'cash_available_for_withdrawal': '314.1500',
                                                    'cash_held_for_dividends': '0.0000',
                                                    'cash_held_for_nummus_restrictions': '0.0000',
                                                    'cash_held_for_options_collateral': '0.0000',
                                                    'cash_held_for_orders': '0.0000',
                                                    'cash_held_for_restrictions': '0.0000',
                                                    'cash_pending_from_options_events': '0.0000',
                                                    'created_at': '2018-10-03T13:56:45.983561Z',
                                                    'crypto_buying_power': '314.1500',
                                                    'day_trade_buying_power': '314.1500',
                                                    'day_trade_buying_power_held_for_orders': '0.0000',
                                                    'day_trade_ratio': '0.25',
                                                    'day_trades_protection': True,
                                                    'funding_hold_balance': '0.0000',
                                                    'gold_equity_requirement': '0.0000',
                                                    'margin_limit': '0.0000',
                                                    'margin_withdrawal_limit': None,
                                                    'marked_pattern_day_trader_date': None,
                                                    'net_moving_cash': '-154.3500',
                                                    'outstanding_interest': '0.0000',
                                                    'overnight_buying_power': '314.1500',
                                                    'overnight_buying_power_held_for_orders': '0.0000',
                                                    'overnight_ratio': '0.50',
                                                    'pending_debit_card_debits': '0.0000',
                                                    'pending_deposit': '0.0000',
                                                    'portfolio_cash': '314.1500',
                                                    'settled_amount_borrowed': '0.0000',
                                                    'sma': '0',
                                                    'start_of_day_dtbp': '765.4000',
                                                    'start_of_day_overnight_buying_power': '760.4000',
                                                    'unallocated_margin_cash': '314.1500',
                                                    'uncleared_deposits': '0.0000',
                                                    'uncleared_nummus_deposits': '0.0000',
                                                    'unsettled_debit': '0.0000',
                                                    'unsettled_funds': '0.0000',
                                                    'updated_at': '2020-02-17T21:02:25.124292Z'},
                            'max_ach_early_access_amount': '25000.00',
                            'only_position_closing_trades': False,
                            'option_level': None,
                            'permanently_deactivated': False,
                            'portfolio': 'https://api.robinhood.com/accounts/8TV36483/portfolio/',
                            'portfolio_cash': '314.1500',
                            'positions': 'https://api.robinhood.com/accounts/8TV36483/positions/',
                            'received_ach_debit_locked': False,
                            'rhs_account_number': 625431924,
                            'sma': '0',
                            'sma_held_for_orders': '0',
                            'state': 'active',
                            'sweep_enabled': True,
                            'type': 'margin',
                            'uncleared_deposits': '0.0000',
                            'unsettled_debit': '0.0000',
                            'unsettled_funds': '0.0000',
                            'updated_at': '2020-02-08T02:47:11.503008Z',
                            'url': 'https://api.robinhood.com/accounts/8TV36483/',
                            'user': 'api.robinhood.com/user/',
                            'withdrawal_halted': False}]}
        """
        response = self.session.get(api.accounts(), timeout=15)
        response.raise_for_status()
        data = response.json()

        return data

    def getAccount(self, accountNumber: str = None):
        """
        Example Response Data:
        {   'account_number': '8TV36483',
            'active_subscription_id': '72d1b8ab-5e00-4472-bef3-6b3437d3bae1',
            'buying_power': '314.1500',
            'can_downgrade_to_cash': 'https://api.robinhood.com/accounts/5QT19448/can_downgrade_to_cash/',
            'cash': '561.3400',
            'cash_available_for_withdrawal': '314.1500',
            'cash_balances': None,
            'cash_held_for_orders': '0.0000',
            'cash_management_enabled': False,
            'created_at': '2017-03-11T18:12:13.256678Z',
            'crypto_buying_power': '314.1500',
            'deactivated': False,
            'deposit_halted': False,
            'drip_enabled': False,
            'eligible_for_drip': False,
            'eligible_for_fractionals': False,
            'instant_eligibility': {   'additional_deposit_needed': '0.0000',
                                        'compliance_user_major_oak_email': None,
                                        'created_at': '2017-03-11T18:12:13.256678Z',
                                        'created_by': None,
                                        'reason': '',
                                        'reinstatement_date': None,
                                        'reversal': None,
                                        'state': 'ok',
                                        'updated_at': None},
            'is_pinnacle_account': True,
            'locked': False,
            'margin_balances': {   'cash': '561.3400',
                                    'cash_available_for_withdrawal': '314.1500',
                                    'cash_held_for_dividends': '0.0000',
                                    'cash_held_for_nummus_restrictions': '0.0000',
                                    'cash_held_for_options_collateral': '0.0000',
                                    'cash_held_for_orders': '0.0000',
                                    'cash_held_for_restrictions': '0.0000',
                                    'cash_pending_from_options_events': '0.0000',
                                    'created_at': '2018-10-03T13:56:45.983561Z',
                                    'crypto_buying_power': '314.1500',
                                    'day_trade_buying_power': '314.1500',
                                    'day_trade_buying_power_held_for_orders': '0.0000',
                                    'day_trade_ratio': '0.25',
                                    'day_trades_protection': True,
                                    'funding_hold_balance': '0.0000',
                                    'gold_equity_requirement': '0.0000',
                                    'margin_limit': '0.0000',
                                    'margin_withdrawal_limit': None,
                                    'marked_pattern_day_trader_date': None,
                                    'net_moving_cash': '-154.3500',
                                    'outstanding_interest': '0.0000',
                                    'overnight_buying_power': '314.1500',
                                    'overnight_buying_power_held_for_orders': '0.0000',
                                    'overnight_ratio': '0.50',
                                    'pending_debit_card_debits': '0.0000',
                                    'pending_deposit': '0.0000',
                                    'portfolio_cash': '314.1500',
                                    'settled_amount_borrowed': '0.0000',
                                    'sma': '0',
                                    'start_of_day_dtbp': '765.4000',
                                    'start_of_day_overnight_buying_power': '760.4000',
                                    'unallocated_margin_cash': '314.1500',
                                    'uncleared_deposits': '0.0000',
                                    'uncleared_nummus_deposits': '0.0000',
                                    'unsettled_debit': '0.0000',
                                    'unsettled_funds': '0.0000',
                                    'updated_at': '2020-02-17T21:02:25.124292Z'},
            'max_ach_early_access_amount': '25000.00',
            'only_position_closing_trades': False,
            'option_level': None,
            'permanently_deactivated': False,
            'portfolio': 'https://api.robinhood.com/accounts/8TV36483/portfolio/',
            'portfolio_cash': '314.1500',
            'positions': 'https://api.robinhood.com/accounts/8TV36483/positions/',
            'received_ach_debit_locked': False,
            'rhs_account_number': 625431924,
            'sma': '0',
            'sma_held_for_orders': '0',
            'state': 'active',
            'sweep_enabled': True,
            'type': 'margin',
            'uncleared_deposits': '0.0000',
            'unsettled_debit': '0.0000',
            'unsettled_funds': '0.0000',
            'updated_at': '2020-02-08T02:47:11.503008Z',
            'url': 'https://api.robinhood.com/accounts/8TV36483/',
            'user': 'api.robinhood.com/user/',
            'withdrawal_halted': False}
        """
        accountNumber = self._getAccountNumberOrDefault(accountNumber)
        response = self.session.get(
            api.accountByNumber(accountNumber), timeout=15
        )
        response.raise_for_status()
        data = response.json()

        return data

    def _getAccountNumberOrDefault(self, accountNumber: str = None):
        """

        """
        allAccounts = self.getAllAccounts()
        firstAccountNumber = allAccounts["results"][0]["account_number"]

        if accountNumber is not None:
            if allAccounts["next"]:
                nextUrl = allAccounts["next"]
                accounts = [allAccounts["results"][0]]

                while nextUrl:
                    response = self.session.get(nextUrl, timeout=15)
                    response.raise_for_status()
                    data = response.json()
                    account = data["results"][0]
                    accounts.append(account)

                for account in accounts:
                    if accountNumber not in account["account_number"]:
                        accountNumber = firstAccountNumber

            else:
                accounts = allAccounts["results"]

                for account in accounts:
                    if accountNumber not in account["account_number"]:
                        accountNumber = firstAccountNumber
        else:
            accountNumber = firstAccountNumber

        return accountNumber

