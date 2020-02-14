import pytest
from Robinhood import Robinhood
from Robinhood.config import getConfiguration


def test_login_qrCode(maintainConfig):
    config = getConfiguration()
    qrCode = input("QR Code: ")
    config.set("login", "qrCode", qrCode)
    with open("config.ini", "w") as configFile:
        config.write(configFile)

    trader = Robinhood()
    trader.login()

    assert trader.session.siteAuthToken != None
    assert trader.session.refreshToken != None
    assert trader.session.headers["Authorization"].startswith("Bearer: ")

