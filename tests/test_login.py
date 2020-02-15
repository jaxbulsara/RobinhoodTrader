import pytest
from RobinhoodTrader import RobinhoodTrader
from RobinhoodTrader.config import getConfiguration

def test_login_logout(maintainConfig):
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
    trader.login()

    assert trader.session.siteAuthToken != None
    assert trader.session.refreshToken != None
    assert trader.session.headers["Authorization"].startswith("Bearer: ")
    assert trader.session.isLoggedIn == True
    assert trader.broker.session == trader.session

    trader.logout()
    
    assert trader.session.siteAuthToken == None
    assert trader.session.headers["Authorization"] == None
    assert trader.session.isLoggedIn == False
    assert trader.broker.session == None


