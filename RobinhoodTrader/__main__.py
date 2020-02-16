from .RobinhoodTrader import RobinhoodTrader
from RobinhoodTrader.config import getConfiguration
import pprint, os, shutil

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

    output = trader.getWatchlistByName("Default")
    printer.pprint(output)

except Exception:
    raise Exception

finally:
    os.remove("config.ini")
    os.rename("config.ini.bak", "config.ini")
    os.chdir("../")
