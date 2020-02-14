import pytest


@pytest.fixture
def maintainConfig():
    os.chdir("Robinhood/")
    shutil.copy2("config.ini", "config.ini.bak")
    yield None
    os.remove("config.ini")
    os.rename("config.ini.bak", "config.ini")
    os.chdir("../")
