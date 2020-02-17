import pytest
from RobinhoodTrader.config import getConfiguration, getQrCode


def test_getConfiguration(maintainConfig):
    config = getConfiguration()

    assert type(config).__name__ == "ConfigParser"
    assert "login" in config.keys()
    assert "qrCodePattern" in config["login"].keys()


def test_getQrCode_NoCode(maintainConfig):
    config = getConfiguration()
    config.remove_option("login", "qrCode")
    with open("config.ini", "w") as configFile:
        config.write(configFile)

    qrCode = getQrCode()

    assert qrCode == None


def test_getQrCode_invalidCode(maintainConfig):
    config = getConfiguration()
    config.set("login", "qrCode", "None")
    with open("config.ini", "w") as configFile:
        config.write(configFile)

    config = getConfiguration()
    qrCode = getQrCode()

    assert qrCode == None


def test_getQrCode_validCode(maintainConfig):
    config = getConfiguration()
    config.set("login", "qrCode", "AAAA1111BBBB2222")
    with open("config.ini", "w") as configFile:
        config.write(configFile)

    qrCode = getQrCode()

    assert qrCode == "AAAA1111BBBB2222"
