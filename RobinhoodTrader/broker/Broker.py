from RobinhoodTrader import endpoints
from RobinhoodTrader.session import RobinhoodSession
import warnings, requests, pprint


class Broker:
    def __init__(self):
        pass

    def getInvestmentProfile(self, session: RobinhoodSession):
        try:
            response = session.get(endpoints.investmentProfile(), timeout=15)
            response.raise_for_status()
            responseData = response.json()
            pprint.pprint(responseData, indent=4)
            return responseData
            
        except requests.exceptions.HTTPError:
            warnings.warn(
                "You must log in before you can access your investment profile."
            )
