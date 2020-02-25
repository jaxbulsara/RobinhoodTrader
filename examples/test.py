from RobinhoodTrader import RobinhoodTrader
from RobinhoodTrader.endpoints import api, nummus

trader = RobinhoodTrader()
trader.login()

response = trader.session.connect(nummus.holdings())
response.raise_for_status()
data = response.json()
trader.printData(data)
