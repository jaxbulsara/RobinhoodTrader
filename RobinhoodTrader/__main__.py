from .RobinhoodTrader import RobinhoodTrader
from RobinhoodTrader.config import getConfiguration
from RobinhoodTrader import endpoints
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

    data = trader.deleteFromWatchlist("f4d089b7-c822-48ac-884d-8ecb312ebb67")
    printer.pprint(data)

    data = trader.addToWatchList(
        "https://api.robinhood.com/instruments/f4d089b7-c822-48ac-884d-8ecb312ebb67/"
    )
    printer.pprint(data)

    watchlist = trader.getWatchlist()
    printer.pprint(watchlist)

except Exception:
    raise Exception

finally:
    os.remove("config.ini")
    os.rename("config.ini.bak", "config.ini")
    os.chdir("../")
