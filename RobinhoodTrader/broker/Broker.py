from RobinhoodTrader import endpoints
import warnings, requests

class Broker:
    def __init__(self):
        pass

    def getInvestmentProfile(self):
        try:
            response = self.session.get(endpoints.investmentProfile(), timeout=15)
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            warnings.warn("You must log in before you can access your investment profile.")
