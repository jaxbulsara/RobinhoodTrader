from .TokenFactory import TokenFactory
from RobinhoodTrader import exceptions
from RobinhoodTrader import endpoints

import requests
from urllib.request import getproxies


class Session:
    def __init__(self):
        self.session = requests.session()
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

    def login(self, username, password, qrCode=None):
        payload = self._generatePayload(username, password, qrCode=qrCode)
        self._getAccessToken(payload, qrCode)

    def _generatePayload(self, username, password, qrCode=None, smsCode=None):
        if qrCode or smsCode:
            payload = self._generatePayloadForLogin(
                username, password, qrCode, smsCode
            )
        else:
            payload = self._generatePayloadForSmsChallenge(username, password)
            smsCode = self._performSmsChallenge(payload)
            payload = self._generatePayload(username, password, smsCode=smsCode)

        return payload

    def _getAccessToken(self, payload, qrCode):
        try:
            loginResponse = self.session.post(
                endpoints.login(), data=payload, timeout=15
            )
            loginResponseData = loginResponse.json()
            self._extractLoginDataTokens(loginResponseData)
        except requests.exceptions.HTTPError:
            self.isLoggedIn = False
            raise exceptions.LoginFailed()

    def _generatePayloadForLogin(
        self, username, password, qrCode=None, smsCode=None
    ):
        payload = {
            "username": username,
            "password": password,
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
        elif smsCode:
            payload["mfa_code"] = smsCode

        return payload

    def _generatePayloadForSmsChallenge(self, username, password):
        payload = {
            "username": username,
            "password": password,
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
            self.headers["Authorization"] = "Bearer: " + self.siteAuthToken
            self.isLoggedIn = True
        else:
            self.isLoggedIn = False
            raise exceptions.InvalidLogin()

    def _performSmsChallenge(self, payload):
        self.session.post(endpoints.login(), data=payload, timeout=15)
        smsCode = input("Type in SMS Code: ")
        return smsCode
