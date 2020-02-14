from .TokenFactory import TokenFactory
from Robinhood import exceptions
from Robinhood import endpoints

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

    def login(self, username, password, qrCode=None):
        payload = self._generatePayload(username, password, qrCode=qrCode)
        self._getAccessToken(payload, qrCode)

    def _generatePayload(self, username, password, qrCode=None):
        if qrCode:
            payload = self._generatePayloadWithQrCode(
                username, password, qrCode
            )
        else:
            payload = self._generatePayloadWithSmsCode(username, password)

        return payload

    def _getAccessToken(self, payload, qrCode):
        try:
            if not qrCode:
                self._performSmsChallenge(payload)

            loginResponse = self.session.post(
                endpoints.login(), data=payload, timeout=15
            )
            loginResponseData = loginResponse.json()
            self._extractLoginDataTokens(loginResponseData)
        except requests.exceptions.HTTPError:
            raise exceptions.LoginFailed()

    def _generatePayloadWithQrCode(self, username, password, qrCode):
        multiFactorAuthToken = self.tokenFactory.generateMultiFactorAuthToken(
            qrCode
        )
        payload = {
            "username": username,
            "password": password,
            "grant_type": "password",
            "client_id": self.clientID,
            "scope": "internal",
            "device_token": self.deviceToken,
            "mfa_code": multiFactorAuthToken,
        }

        return payload

    def _generatePayloadWithSmsCode(self, username, password):
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
        else:
            raise exceptions.InvalidLogin()

    def _performSmsChallenge(self, payload):
        initialResponse = self.session.post(
            endpoints.login(), data=payload, timeout=15
        )
        initialResponseData = initialResponse.json()
        challengeID = initialResponseData["challenge"]["id"]
        self.headers["X-ROBINHOOD-CHALLENGE-RESPONSE-ID"] = challengeID
        smsCode = input("Type in SMS Code: ")
        challengeResponse = {"response": smsCode}
        smsChallengeResponse = self.session.post(
            endpoints.smsChallenge(challengeID),
            data=challengeResponse,
            timeout=15,
        )
        smsChallengeResponse.raise_for_status()
