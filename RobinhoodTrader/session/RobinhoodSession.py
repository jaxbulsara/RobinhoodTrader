from .TokenFactory import TokenFactory
from RobinhoodTrader import exceptions
from RobinhoodTrader import endpoints
from RobinhoodTrader.config import getQrCode

import requests, platform, warnings, sys
from getpass import getpass
from urllib.request import getproxies


class RobinhoodSession(requests.Session):
    def __init__(self):
        super(RobinhoodSession, self).__init__()
        self.proxies = getproxies()
        self.tokenFactory = TokenFactory()
        self.deviceToken = self.tokenFactory.generateDeviceToken()
        self.clientID = "c82SH0WZOsabOXGP2sxqcj34FxkvfnWRZBKlBjFS"
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

    def login(self, credentials=(None, None)):
        if None in credentials and self.sessionIsConsole:
            credentials = self._getCredentialsFromUser()
        else:
            raise exceptions.CredentialError()

        if None in credentials:
            print("Login cancelled.")
        else:
            qrCode = getQrCode()
            payload = self._generatePayload(credentials, qrCode=qrCode)
            self._getAccessToken(payload, qrCode)

    def logout(self):
        try:
            payload = {
                "client_id": self.clientID,
                "token": self.refreshToken,
            }

            logoutRequest = self.post(
                endpoints.logout(), data=payload, timeout=15
            )
            logoutRequest.raise_for_status()
        except requests.exceptions.HTTPError as errorMessage:
            warnings.warn(f"Failed to logout {repr(errorMessage)}")

        self.headers["Authorization"] = None
        self.siteAuthToken = None
        self.isLoggedIn = False

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
            payload = self._generatePayload(credentials, manualCode=manualCode)

        return payload

    def _getAccessToken(self, payload, qrCode):
        try:
            loginResponse = self.post(
                endpoints.login(), data=payload, timeout=15
            )
            loginResponseData = loginResponse.json()
            self._extractLoginDataTokens(loginResponseData)
        except requests.exceptions.HTTPError:
            raise exceptions.LoginFailed()

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
            multiFactorAuthToken = self.tokenFactory.generateMultiFactorAuthToken(
                qrCode
            )
            payload["mfa_code"] = multiFactorAuthToken
        elif manualCode:
            payload["mfa_code"] = manualCode

        return payload

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

    def _extractLoginDataTokens(self, loginResponseData):
        dataHasAccessToken = "access_token" in loginResponseData.keys()
        dataHasRefreshToken = "refresh_token" in loginResponseData.keys()

        if dataHasAccessToken and dataHasRefreshToken:
            self.siteAuthToken = loginResponseData["access_token"]
            self.refreshToken = loginResponseData["refresh_token"]
            self.headers["Authorization"] = f"Bearer {self.siteAuthToken}"
            self.isLoggedIn = True
        else:
            warnings.warn(
                "Unable to login. Please enter different credentials and try again."
            )
            self.login()

    def _performManualChallenge(self, payload):
        self.post(endpoints.login(), data=payload, timeout=15)
        manualCode = input("Type in code from SMS or Authenticator app: ")
        return manualCode
