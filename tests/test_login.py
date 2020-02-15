import pytest
from RobinhoodTrader import Robinhood
from RobinhoodTrader.config import getConfiguration


def test_login(maintainConfig):
    config = getConfiguration()
    qrCode = input("QR Code (Leave blank for SMS challenge): ")
    if qrCode == "":
        qrCode = "None"
    config.set("login", "qrCode", qrCode)
    with open("config.ini", "w") as configFile:
        config.write(configFile)

    trader = Robinhood()
    trader.login()

    assert trader.session.siteAuthToken != None
    assert trader.session.refreshToken != None
    assert trader.session.headers["Authorization"].startswith("Bearer: ")
