from configparser import ConfigParser
import re, os, pathlib


def getConfiguration():
    originalWorkingDirectory = os.getcwd()
    thisFileDirectory = os.path.dirname(pathlib.Path(__file__))

    os.chdir(thisFileDirectory)

    configParser = ConfigParser()
    configParser.read("config.ini")

    os.chdir(originalWorkingDirectory)

    return configParser


def getQrCode():
    config = getConfiguration()
    qrCode = config.get("login", "qrCode", fallback=None)
    qrCode = _checkQrCode(config, qrCode)

    return qrCode


def _checkQrCode(config, qrCode):
    if qrCode:
        qrCodePattern = config.get("login", "qrCodePattern")
        qrCodeIsValid = re.match(qrCodePattern, qrCode)
        if qrCodeIsValid:
            qrCode = qrCode
        else:
            qrCode = None

    return qrCode
