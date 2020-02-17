import random
import time, base64, struct, hmac, hashlib


class TokenFactory:
    def __init__(self):
        pass

    def generateMultiFactorAuthToken(self, qrCode, currentTimeSeed=None):
        if currentTimeSeed is None:
            currentTimeSeed = int(time.time()) // 30

        cStructSeed = struct.pack(">Q", currentTimeSeed)
        cStructKey = base64.b32decode(qrCode, True)
        hmacObject = hmac.new(cStructKey, cStructSeed, hashlib.sha1)
        hmacDigest = hmacObject.digest()
        authToken = self._getMultiFactorAuthToken(hmacDigest)

        return authToken

    def _getMultiFactorAuthToken(self, hmacDigest):
        authTokenStartPosition = hmacDigest[19] & 0b1111
        authTokenEndPosition = authTokenStartPosition + 4
        authToken = struct.unpack(
            ">I", hmacDigest[authTokenStartPosition:authTokenEndPosition]
        )[0]
        authToken &= 0x7FFFFFFF
        authToken %= 1000000
        authToken = f"{authToken:06d}"

        return authToken
