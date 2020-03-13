from RobinhoodTrader import RobinhoodTrader
from RobinhoodTrader.endpoints import api, nummus
import pprint

trader = RobinhoodTrader()
trader.login()

payload = {"owner_type": "custom"}
data = trader.session.get(api.midlands_lists(), data=payload)
print(data)
pprint.pprint(data.json(), indent=4)
