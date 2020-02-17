from .RobinhoodTrader import RobinhoodTrader
from RobinhoodTrader.config import getConfiguration
from RobinhoodTrader import apiEndpoints, nummusEndpoints
import pprint, os, shutil, requests, json

printer = pprint.PrettyPrinter(indent=4)
os.chdir("RobinhoodTrader/")
shutil.copy2("config.ini", "config.ini.bak")
if os.path.isfile("myConfig.ini"):
    os.remove("config.ini")
    shutil.copy2("myConfig.ini", "config.ini")

try:
    trader = RobinhoodTrader()
    config = getConfiguration()
    username = config.get("login", "username", fallback=None)
    password = config.get("login", "password", fallback=None)
    credentials = (username, password)
    trader.login(credentials)

    data = trader.cryptoBroker.getWatchlistCurrencyPairIds()
    printer.pprint(data)

    data = trader.cryptoBroker.addToWatchlist(
        "b9729798-2aec-4ca9-8637-4d9789d63764"
    )
    printer.pprint(data)

    data = trader.cryptoBroker.getWatchlistCurrencyPairIds()
    printer.pprint(data)


except Exception:
    raise Exception

finally:
    os.remove("config.ini")
    os.rename("config.ini.bak", "config.ini")
    os.chdir("../")
