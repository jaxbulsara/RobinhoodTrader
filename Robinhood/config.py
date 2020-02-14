from configparser import ConfigParser
from Robinhood.utility import LogFactory
import re


def getConfiguration():
    configParser = ConfigParser()
    configParser.read("config.ini")
    return configParser


def getQrCode():
    config = getConfiguration()
    qrCode = config.get("login", "qrCode", fallback=None)
    qrCode = _checkQrCode(config, qrCode)

    return qrCode


def _checkQrCode(config, qrCode):
    logFactory = LogFactory()
    log = logFactory.getLogger()
    if qrCode:
        qrCodePattern = config.get("login", "qrCodePattern")
        qrCodeIsValid = re.match(qrCodePattern, qrCode)
        if qrCodeIsValid:
            qrCode = qrCode
        else:
            log.info("QR code in config.ini is not in the correct format.")
            qrCode = None

    return qrCode

