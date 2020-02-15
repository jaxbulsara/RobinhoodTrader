import pytest
import shutil
import os


@pytest.fixture
def maintainConfig():
    os.chdir("RobinhoodTrader/")
    shutil.copy2("config.ini", "config.ini.bak")
    yield None
    os.remove("config.ini")
    os.rename("config.ini.bak", "config.ini")
    os.chdir("../")
