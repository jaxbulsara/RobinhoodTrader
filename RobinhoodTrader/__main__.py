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

    data = trader.getWatchlistInstrumentIds()
    printer.pprint(data)

    data = trader.deleteMultipleFromWatchlist(
        [
            "e39ed23a-7bd1-4587-b060-71988d9ef483",
            "54db869e-f7d5-45fb-88f1-8d7072d4c8b2",
        ]
    )
    printer.pprint(data)

    data = trader.getWatchlistInstrumentIds()
    printer.pprint(data)

    data = trader.addMultipleToWatchlist(
        [
            endpoints.instruments() + "e39ed23a-7bd1-4587-b060-71988d9ef483/",
            endpoints.instruments() + "54db869e-f7d5-45fb-88f1-8d7072d4c8b2/",
        ]
    )
    printer.pprint(data)

    data = trader.getWatchlistInstrumentIds()
    printer.pprint(data)


except Exception:
    raise Exception

finally:
    os.remove("config.ini")
    os.rename("config.ini.bak", "config.ini")
    os.chdir("../")
