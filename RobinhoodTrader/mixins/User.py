from __future__ import absolute_import
from ..RobinhoodSession import RobinhoodSession
from ..endpoints import api
from ..wrappers import authRequired


class User:
    @authRequired
    def getInvestmentProfile(self):
        """
        Example response:
        {   'annual_income': '0_25000',
            'interested_in_options': None,
            'investment_experience': 'no_investment_exp',
            'investment_experience_collected': False,
            'investment_objective': 'cap_preserve_invest_obj',
            'liquid_net_worth': '0_25000',
            'liquidity_needs': 'not_important_liq_need',
            'option_trading_experience': '',
            'professional_trader': None,
            'risk_tolerance': 'low_risk_tolerance',
            'source_of_funds': 'savings_personal_income',
            'suitability_verified': True,
            'tax_bracket': '',
            'time_horizon': 'short_time_horizon',
            'total_net_worth': '0_25000',
            'understand_option_spreads': None,
            'updated_at': '2019-10-13T17:34:12.129384Z',
            'user': 'api.robinhood.com/user/'}
        """

        response = self.session.get(api.userInvestmentProfile(), timeout=15)
        response.raise_for_status()
        data = response.json()

        return data
