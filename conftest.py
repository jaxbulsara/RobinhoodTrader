import pytest
import shutil
import os
from RobinhoodTrader import RobinhoodTrader
from RobinhoodTrader.config import getConfiguration


@pytest.fixture(scope="session")
def maintainConfig():
    os.chdir("RobinhoodTrader/")
    shutil.copy2("config.ini", "config.ini.bak")
    yield None
    os.remove("config.ini")
    os.rename("config.ini.bak", "config.ini")
    os.chdir("../")


@pytest.fixture(scope="session")
def robinhoodTrader(maintainConfig):
    config = getConfiguration()
    qrCode = input(
        "QR Code (Leave blank to use SMS or Authenticator app code): "
    )
    if qrCode == "":
        qrCode = "None"
    config.set("login", "qrCode", qrCode)
    with open("config.ini", "w") as configFile:
        config.write(configFile)

    trader = RobinhoodTrader()

    yield trader

    trader.logout()

    assert trader.session.siteAuthToken == None
    assert trader.session.headers["Authorization"] == None
    assert trader.session.isLoggedIn == False