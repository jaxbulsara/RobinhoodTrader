from Robinhood.utility import TokenFactory
import re


def test_deviceToken():
    tokenFactory = TokenFactory()
    deviceToken = tokenFactory.generateDeviceToken()
    deviceTokenPattern = (
        "[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}"
    )

    assert re.match(deviceTokenPattern, deviceToken)


def test_multiFactorAuthToken():
    encoded32BitKey = "AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH"
    currentFormattedTime = 52723281
    expectedAuthToken = "962722"
    tokenFactory = TokenFactory()
    authToken = tokenFactory.generateMultiFactorAuthToken(
        encoded32BitKey, currentFormattedTime
    )
    assert authToken == expectedAuthToken
