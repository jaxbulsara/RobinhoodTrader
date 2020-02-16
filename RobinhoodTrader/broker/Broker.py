from RobinhoodTrader import endpoints
from RobinhoodTrader.session import RobinhoodSession


class Broker:
    def getInvestmentProfile(self, session: RobinhoodSession):
        response = session.get(endpoints.userInvestmentProfile(), timeout=15,)
        response.raise_for_status()
        responseData = response.json()
        return responseData
