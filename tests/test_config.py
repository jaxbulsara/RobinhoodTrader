import pytest
from configparser import ConfigParser
from RobinhoodTrader.config import get_configuration, get_qr_code


def test__get_configuration(maintain_config):
    config = get_configuration()

    assert type(config) == ConfigParser
    assert "login" in config.keys()
    assert "username" in config["login"].keys()
    assert "password" in config["login"].keys()
    assert "qr_code" in config["login"].keys()


def test__get_qr_code__no_code(maintain_config):
    config = get_configuration()
    config.remove_option("login", "qr_code")
    with open("config.ini", "w") as configFile:
        config.write(configFile)

    qr_code = get_qr_code()

    assert qr_code == None


def test__get_qr_code__invalid_code(maintain_config):
    config = get_configuration()
    config.set("login", "qr_code", "None")
    with open("config.ini", "w") as configFile:
        config.write(configFile)

    config = get_configuration()
    qr_code = get_qr_code()

    assert qr_code == None


def test__get_qr_code__valid_code(maintain_config):
    config = get_configuration()
    config.set("login", "qr_code", "AAAA1111BBBB2222")
    with open("config.ini", "w") as configFile:
        config.write(configFile)

    qr_code = get_qr_code()

    assert qr_code == "AAAA1111BBBB2222"
