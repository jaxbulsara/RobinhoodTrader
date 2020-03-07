import pytest, shutil, os, re
from RobinhoodTrader import RobinhoodTrader
from RobinhoodTrader.config import get_configuration
from RobinhoodTrader.exceptions import LoginError


@pytest.fixture
def maintain_config():
    shutil.copy2("config.ini", "config.ini.bak1")

    yield None

    os.remove("config.ini")
    os.rename("config.ini.bak1", "config.ini")


@pytest.fixture(scope="session")
def use_my_config():
    shutil.copy2("config.ini", "config.ini.bak2")

    if os.path.isfile("myconfig.ini"):
        os.remove("config.ini")
        shutil.copy2("myconfig.ini", "config.ini")

    yield None

    os.remove("config.ini")
    os.rename("config.ini.bak2", "config.ini")


@pytest.fixture(scope="session")
def trader(use_my_config):
    trader = RobinhoodTrader()

    with pytest.raises(LoginError):
        trader.login(("user", "pass"))

    try:
        trader.login()
    except LoginError:
        trader.login(use_config=False)

    assert trader.session.site_auth_token != None
    assert trader.session.refresh_token != None
    assert re.match("Bearer .+", trader.session.headers["Authorization"])
    assert trader.session.is_logged_in == True

    yield trader

    trader.logout()

    assert trader.session.site_auth_token == None
    assert trader.session.headers["Authorization"] == None
    assert trader.session.is_logged_in == False
