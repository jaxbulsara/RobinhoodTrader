import random
import time, base64, struct, hmac, hashlib


class TokenFactory:
    def __init__(self):
        pass

    def generateDeviceToken(self):
        randomHexIndices = self._createRandomHexIndices()
        hexPairs = self._createHexPairs()
        deviceToken = self._createDeviceToken(randomHexIndices, hexPairs)
        return deviceToken

    def generateMultiFactorAuthToken(self, secret, currentTimeSeed=None):
        if currentTimeSeed is None:
            currentTimeSeed = int(time.time()) // 30

        cStructSeed = struct.pack(">Q", currentTimeSeed)
        cStructKey = base64.b32decode(secret, True)
        hmacObject = hmac.new(cStructKey, cStructSeed, hashlib.sha1)
        hmacDigest = hmacObject.digest()
        authToken = self._getMultiFactorAuthToken(hmacDigest)

        return authToken

    def _createRandomHexIndices(self):
        hexIndexPositions = range(0, 16)
        randomHexIndices = list(
            map(
                lambda position: self._getRandomByte(
                    position, self._generateRandom32BitInt()
                ),
                hexIndexPositions,
            )
        )

        return randomHexIndices

    def _getRandomByte(self, position, random32BitInt):
        # 0011 & 0000 == 0000 (0) -> a
        # 0011 & 0001 == 0001 (1)
        # 0011 & 0010 == 0010 (2)
        # 0011 & 0011 == 0011 (3)
        # 0011 & 0100 == 0000 (0)

        fourCount = 0b0011 & position

        # 0000 << 3 == 0000000 (0) -> b
        # 0001 << 3 == 0001000 (8)
        # 0010 << 3 == 0010000 (16)
        # 0011 << 3 == 0011000 (24)
        byteOffset = fourCount << 3
        offsetRandomNumber = random32BitInt >> byteOffset
        randomByte = offsetRandomNumber % 0b11111111
        return randomByte

    def _generateRandom32BitInt(self):
        randomNumber = random.random()
        random32BitInt = int(pow(2, 32) * randomNumber)
        return random32BitInt

    def _createHexPairs(self):
        hexPositions = range(0, 256)
        hexPairs = list(
            map(lambda position: self._getHexPair(position), hexPositions)
        )

        return hexPairs

    def _getHexPair(self, position):
        hexNumber = hex(position + 256)
        hexNumberWithoutPrefix = hexNumber.lstrip("0x")
        hexNumberWithoutLongSuffix = hexNumberWithoutPrefix.rstrip("L")
        nextHexNumber = hexNumberWithoutLongSuffix[1:]
        return nextHexNumber

    def _createDeviceToken(self, randomHexIndices, hexPairs):
        deviceToken = ""
        hyphenPositions = [3, 5, 7, 9]
        for position in range(0, 16):
            deviceToken += hexPairs[randomHexIndices[position]]

            if position in hyphenPositions:
                deviceToken += "-"

        return deviceToken

    def _getCurrentTimeSeed(self):
        pass

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
