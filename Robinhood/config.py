from configparser import ConfigParser
import re


def getConfiguration():
    configParser = ConfigParser()
    configParser.read("config.ini")
    return configParser


def getQrCode():
    config = getConfiguration()
    qrCode = _readQrCode(config)
    qrCode = _checkQrCode(config, qrCode)

    return qrCode


def _readQrCode(config):
    try:
        qrCode = config["login"]["qrCode"]

    except KeyError:
        print("QR code was not found in config.ini.")
        qrCode = None

    return qrCode


def _checkQrCode(config, qrCode):
    if qrCode is not None:
        qrCodePattern = config["login"]["qrCodePattern"]
        qrCodeIsValid = re.match(qrCodePattern, qrCode) is not None
        if qrCodeIsValid:
            qrCode = qrCode
        else:
            print("QR code in config.ini is not in the correct format.")
            print(
                "QR code must be a 32 bit string containing only the characters A-Z or 2-7"
            )
            qrCode = None

    return qrCode

