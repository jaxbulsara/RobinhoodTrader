from __future__ import absolute_import
from ..RobinhoodSession import RobinhoodSession
from ..endpoints import api
from ..wrappers import authRequired


class User:
    session: RobinhoodSession

    @authRequired
    def getUser(self) -> dict:
        endpoint = api.user()
        return self.session.getData(endpoint, timeout=15)

    @authRequired
    def getUserBasicInfo(self) -> dict:
        endpoint = api.userBasicInfo()
        return self.session.getData(endpoint, timeout=15)

    @authRequired
    def getUserAdditionalInfo(self) -> dict:
        endpoint = api.userAdditionalInfo()
        return self.session.getData(endpoint, timeout=15)

    @authRequired
    def getUserCipQuestions(self) -> list:
        endpoint = api.userCipQuestions()
        return self.session.getData(endpoint, timeout=15)

    @authRequired
    def getUserEmployment(self) -> dict:
        endpoint = api.userEmployment()
        return self.session.getData(endpoint, timeout=15)

    @authRequired
    def getUserIdentityMismatch(self) -> dict:
        endpoint = api.userIdentityMismatch()
        return self.session.getData(endpoint, timeout=15)

    @authRequired
    def getUserInvestmentProfile(self) -> dict:
        endpoint = api.userInvestmentProfile()
        return self.session.getData(endpoint, timeout=15)
