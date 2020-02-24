from __future__ import absolute_import
from ..RobinhoodSession import RobinhoodSession
from ..endpoints import api
from ..wrappers import authRequired


class User:
    session: RobinhoodSession

    @authRequired
    def getUser(self) -> dict:
        response = self.session.get(api.user(), timeout=15)
        response.raise_for_status()
        data = response.json()

        return data

    @authRequired
    def getUserBasicInfo(self) -> dict:
        response = self.session.get(api.userBasicInfo(), timeout=15)
        response.raise_for_status()
        data = response.json()

        return data

    @authRequired
    def getUserAdditionalInfo(self) -> dict:
        response = self.session.get(api.userAdditionalInfo(), timeout=15)
        response.raise_for_status()
        data = response.json()

        return data

    @authRequired
    def getUserCipQuestions(self) -> list:
        response = self.session.get(api.userCipQuestions(), timeout=15)
        response.raise_for_status()
        data = response.json()

        return data

    @authRequired
    def getUserEmployment(self) -> dict:
        response = self.session.get(api.userEmployment(), timeout=15)
        response.raise_for_status()
        data = response.json()

        return data

    @authRequired
    def getUserIdentityMismatch(self) -> dict:
        response = self.session.get(api.userIdentityMismatch(), timeout=15)
        response.raise_for_status()
        data = response.json()

        return data

    @authRequired
    def getUserInvestmentProfile(self) -> dict:
        response = self.session.get(api.userInvestmentProfile(), timeout=15)
        response.raise_for_status()
        data = response.json()

        return data
