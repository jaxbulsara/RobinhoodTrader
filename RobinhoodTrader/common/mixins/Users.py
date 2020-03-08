from __future__ import absolute_import

from ...RobinhoodTrader import RobinhoodSession
from ...wrappers import auth_required
from ...endpoints import api
from ...datatypes import (
    User,
    UserBasicInfo,
    UserAdditionalInfo,
    UserCipQuestions,
    UserEmployment,
    Page,
    UserInvestmentProfile,
)


class Users:
    session: RobinhoodSession

    @auth_required
    def get_user(self):
        endpoint = api.user()
        data = self.session.get_data(endpoint, timeout=15)
        return User(data)

    @auth_required
    def get_user_basic_info(self):
        endpoint = api.user_basic_info()
        data = self.session.get_data(endpoint, timeout=15)
        return UserBasicInfo(data)

    @auth_required
    def get_user_additional_info(self):
        endpoint = api.user_additional_info()
        data = self.session.get_data(endpoint, timeout=15)
        return UserAdditionalInfo(data)

    @auth_required
    def get_user_cip_questions(self):
        endpoint = api.user_cip_questions()
        data = self.session.get_data(endpoint, timeout=15)
        return UserCipQuestions(data)

    @auth_required
    def get_user_employment(self):
        endpoint = api.user_employment()
        data = self.session.get_data(endpoint, timeout=15)
        return UserEmployment(data)

    @auth_required
    def get_user_identity_mismatch(self):
        endpoint = api.user_identity_mismatch()
        data = self.session.get_data(endpoint, timeout=15)
        return Page(data)

    @auth_required
    def get_user_investment_profile(self):
        endpoint = api.user_investment_profile()
        data = self.session.get_data(endpoint, timeout=15)
        return UserInvestmentProfile(data)
