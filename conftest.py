import pytest, shutil, os, re
from RobinhoodTrader import RobinhoodTrader
from RobinhoodTrader.config import getConfiguration


@pytest.fixture
def maintainConfig():
    os.chdir("RobinhoodTrader/")
    shutil.copy2("config.ini", "config.ini.bak")
    yield None
    os.remove("config.ini")
    os.rename("config.ini.bak", "config.ini")
    os.chdir("../")


@pytest.fixture(scope="session")
def useMyConfig():
    os.chdir("RobinhoodTrader/")
    shutil.copy2("config.ini", "config.ini.bak")
    if os.path.isfile("myConfig.ini"):
        os.remove("config.ini")
        shutil.copy2("myConfig.ini", "config.ini")
    yield None
    os.remove("config.ini")
    os.rename("config.ini.bak", "config.ini")
    os.chdir("../")


@pytest.fixture(scope="session")
def robinhoodTrader(useMyConfig):
    trader = RobinhoodTrader()
    trader.login()

    assert trader.session.siteAuthToken != None
    assert trader.session.refreshToken != None
    assert re.match("Bearer .+", trader.session.headers["Authorization"])
    assert trader.session.isLoggedIn == True

    yield trader

    trader.logout()

    assert trader.session.siteAuthToken == None
    assert trader.session.headers["Authorization"] == None
    assert trader.session.isLoggedIn == False
