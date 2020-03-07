from __future__ import absolute_import

from ...RobinhoodTrader import RobinhoodSession
from ...wrappers import auth_required
from ...endpoints import api


class Users:
    session: RobinhoodSession

    @auth_required
    def get_user(self):
        endpoint = api.user()
        return self.session.get_data(endpoint, timeout=15)

    @auth_required
    def get_user_basic_info(self):
        endpoint = api.user_basic_info()
        return self.session.get_data(endpoint, timeout=15)

    @auth_required
    def get_user_additional_info(self):
        endpoint = api.user_additional_info()
        return self.session.get_data(endpoint, timeout=15)

    @auth_required
    def get_user_cip_questions(self):
        endpoint = api.user_cip_questions()
        return self.session.get_data(endpoint, timeout=15)

    @auth_required
    def get_user_employment(self):
        endpoint = api.user_employment()
        return self.session.get_data(endpoint, timeout=15)

    @auth_required
    def get_user_identity_mismatch(self):
        endpoint = api.user_identity_mismatch()
        return self.session.get_data(endpoint, timeout=15)

    @auth_required
    def get_user_investment_profile(self):
        endpoint = api.user_investment_profile()
        return self.session.get_data(endpoint, timeout=15)
