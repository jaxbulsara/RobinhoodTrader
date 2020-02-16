from RobinhoodTrader import endpoints
from RobinhoodTrader.session import RobinhoodSession
import warnings, requests


class Broker:
    def getInvestmentProfile(self, session: RobinhoodSession):
        response = session.get(endpoints.investmentProfile(), timeout=15,)
        response.raise_for_status()
        responseData = response.json()
        return responseData

    def getAccounts(self, session: RobinhoodSession):
        pass
