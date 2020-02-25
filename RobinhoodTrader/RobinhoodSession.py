from __future__ import absolute_import
from . import exceptions
from .wrappers import authRequired
from .endpoints import api
from .config import getQrCode

import requests, platform, sys, uuid, time, struct, base64, hmac, hashlib
from getpass import getpass
from urllib.request import getproxies


class RobinhoodSession(requests.Session):
    def __init__(self):
        super(RobinhoodSession, self).__init__()
        self.proxies = getproxies()
        self.deviceToken = str(uuid.uuid4())
        self.clientID = "c82SH0WZOsabOXGP2sxqcj34FxkvfnWRZBKlBjFS"
        self.credentials = (None, None)
        self.siteAuthToken = None
        self.refreshToken = None
        self.headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en;q=1, fr;q=0.9, de;q=0.8, ja;q=0.7, nl;q=0.6, it;q=0.5",
            "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
            "X-Robinhood-API-Version": "1.0.0",
            "Connection": "keep-alive",
            "User-Agent": "Robinhood/823 (iPhone; iOS 7.1.2; Scale/2.00)",
        }
        self.isLoggedIn = False
        self.sessionIsConsole = sys.stdout.isatty()
        self.accountNumbers = None

    def login(self, credentials=(None, None)):
        if None in credentials:
            credentials = self._getCredentialsFromUser()
            if not self.sessionIsConsole:
                raise exceptions.CredentialError()

        if None in credentials:
            print("Login cancelled.")
        else:
            self.credentials = credentials
            qrCode = getQrCode()
            payload = self._generatePayload(credentials, qrCode=qrCode)
            self._getAccessToken(payload, qrCode)
            self._getAccountNumbers()

    def logout(self):
        try:
            payload = {
                "client_id": self.clientID,
                "token": self.refreshToken,
            }

            logoutRequest = self.post(
                api.revokeToken(), data=payload, timeout=15
            )
            logoutRequest.raise_for_status()
        except requests.exceptions.HTTPError:
            print(f"Failed to logout.")
        except requests.exceptions.ConnectionError:
            print(
                f"Failed to connect. Please check your internet and try again."
            )

        self._clearSessionInfo()

    def getData(self, *args, **kwargs) -> dict:
        response = self.get(*args, **kwargs)
        response.raise_for_status()
        data = response.json
        return data

    def headData(self, *args, **kwargs) -> dict:
        response = self.head(*args, **kwargs)
        response.raise_for_status()
        data = response.json
        return data

    def postData(self, *args, **kwargs) -> dict:
        response = self.post(*args, **kwargs)
        response.raise_for_status()
        data = response.json
        return data

    def putData(self, *args, **kwargs) -> dict:
        response = self.put(*args, **kwargs)
        response.raise_for_status()
        data = response.json
        return data

    def deleteData(self, *args, **kwargs) -> dict:
        response = self.delete(*args, **kwargs)
        response.raise_for_status()
        data = response.json
        return data

    def optionsData(self, *args, **kwargs) -> dict:
        response = self.options(*args, **kwargs)
        response.raise_for_status()
        data = response.json
        return data

    def patchData(self, *args, **kwargs) -> dict:
        response = self.patch(*args, **kwargs)
        response.raise_for_status()
        data = response.json
        return data

    def _getCredentialsFromUser(self):
        print("Press Enter to cancel.")
        username = input("Username: ")
        if username != "":
            password = getpass(prompt="Password: ")
        else:
            password = None

        return (username, password)

    def _generatePayload(self, credentials, qrCode=None, manualCode=None):
        if qrCode or manualCode:
            payload = self._generatePayloadForLogin(
                credentials, qrCode, manualCode
            )
        else:
            payload = self._generatePayloadForManualChallenge(credentials)
            manualCode = self._performManualChallenge(payload)
            payload = self._generatePayloadForLogin(
                credentials, qrCode, manualCode
            )

        return payload

    def _getAccessToken(self, payload, qrCode):
        try:
            loginResponse = self.post(api.token(), data=payload, timeout=15)
            loginData = loginResponse.json()
            self._extractLoginDataTokens(loginData)
        except requests.exceptions.HTTPError:
            print(f"Failed to login.")
            raise exceptions.LoginError()
        except requests.exceptions.ConnectionError:
            print(
                f"Failed to connect. Please check your internet and try again."
            )

    def _generatePayloadForLogin(
        self, credentials, qrCode=None, manualCode=None
    ):
        payload = {
            "username": credentials[0],
            "password": credentials[1],
            "grant_type": "password",
            "client_id": self.clientID,
            "scope": "internal",
            "device_token": self.deviceToken,
        }

        if qrCode:
            multiFactorAuthToken = self._generateMultiFactorAuthToken(qrCode)
            payload["mfa_code"] = multiFactorAuthToken
        elif manualCode:
            payload["mfa_code"] = manualCode

        return payload

    def _generateMultiFactorAuthToken(self, qrCode, currentTimeSeed=None):
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

    def _generatePayloadForManualChallenge(self, credentials):
        payload = {
            "username": credentials[0],
            "password": credentials[1],
            "grant_type": "password",
            "client_id": self.clientID,
            "expires_in": "86400",
            "scope": "internal",
            "device_token": self.deviceToken,
            "challenge_type": "sms",
        }

        return payload

    def _performManualChallenge(self, payload):
        self.post(api.token(), data=payload, timeout=15)
        manualCode = input("Type in code from SMS or Authenticator app: ")
        return manualCode

    def _extractLoginDataTokens(self, loginData):
        dataHasAccessToken = "access_token" in loginData.keys()
        dataHasRefreshToken = "refresh_token" in loginData.keys()

        if dataHasAccessToken and dataHasRefreshToken:
            self.siteAuthToken = loginData["access_token"]
            self.refreshToken = loginData["refresh_token"]
            self.headers["Authorization"] = f"Bearer {self.siteAuthToken}"
            self.isLoggedIn = True
        else:
            print(
                "Unable to login. Please enter different credentials and try again."
            )
            self.login()

    @authRequired
    def _getAccountNumbers(self):
        accountsResponse = self.get(api.accounts(), timeout=15)
        accountsResponse.raise_for_status()
        accountsData = accountsResponse.json()
        self.accountNumbers = list(
            map(
                lambda account: account["account_number"],
                accountsData["results"],
            )
        )
        return self.accountNumbers

    def _clearSessionInfo(self):
        self.headers["Authorization"] = None
        self.siteAuthToken = None
        self.isLoggedIn = False
        self.accountNumbers = None
