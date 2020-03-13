from __future__ import absolute_import

from ..exceptions import LoginError
from ..wrappers import auth_required
from ..endpoints import api
from ..config import get_configuration, get_qr_code

from .mixins import HTTPDataMixin

import requests, platform, sys, uuid, time, struct, base64, hmac, hashlib
from getpass import getpass
from urllib.request import getproxies


class RobinhoodSession(requests.Session, HTTPDataMixin):
    def __init__(self, credentials=(None, None), qr_code=None):
        super(RobinhoodSession, self).__init__()
        self.proxies = getproxies()
        self.device_token = str(uuid.uuid4())
        self.client_id = "c82SH0WZOsabOXGP2sxqcj34FxkvfnWRZBKlBjFS"
        self.credentials = credentials
        self.qr_code = qr_code
        self.manual_code = None
        self.login_data = None
        self.payload = None
        self.site_auth_token = None
        self.refresh_token = None
        self.headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en;q=1, fr;q=0.9, de;q=0.8, ja;q=0.7, nl;q=0.6, it;q=0.5",
            "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
            "X-Robinhood-API-Version": "1.0.0",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
        }
        self.is_logged_in = False
        self.session_is_console = sys.stdout.isatty()

        if None not in self.credentials:
            self.login()

    def login(self, credentials=(None, None), qr_code=None, use_config=True):
        self.credentials = credentials
        if None in self.credentials and use_config:
            self._get_credentials_from_config()

        if None in self.credentials:
            self._get_credentials_from_console()

        if None in self.credentials:
            print("Login cancelled.")
        else:
            self._perform_login()

        self._clear_credentials()

    def logout(self):
        endpoint = api.revoke_token()
        self.payload = {
            "client_id": self.client_id,
            "token": self.refresh_token,
        }

        logout_request = self.post(endpoint, data=self.payload, timeout=15)
        logout_request.raise_for_status()

        self._clear_session_info()

    def _get_credentials_from_config(self):
        config = get_configuration()
        username = config.get("login", "username", fallback=None)
        password = config.get("login", "password", fallback=None)

        if username == "None":
            username = None
        if password == "None":
            password = None

        self.credentials = (username, password)

    def _get_credentials_from_console(self):
        if self.session_is_console:
            self._get_credentials_from_user()
        else:
            raise ValueError(
                "This method is not being called in an interactive console. Must pass a non-null tuple of credentials."
            )

    def _get_credentials_from_user(self):
        username, password = self.credentials

        print("Press Enter to cancel.")
        if not username:
            username = input("Username: ")

        if username:
            password = getpass(prompt="Password: ")
        else:
            password = None

        self.credentials = (username, password)

    def _perform_login(self):
        if not self.qr_code:
            self.qr_code = get_qr_code()
        self._generate_payload()
        self._get_access_token()

    def _generate_payload(self):
        if self.qr_code or self.manual_code:
            self._generate_payload_for_login()
        else:
            self._generate_payload_for_manual_challenge()
            self._perform_manual_challenge()
            self._generate_payload_for_login()

    def _get_access_token(self):
        try:
            self.login_data = self.post_data(
                api.token(), data=self.payload, timeout=15
            )
            self._extract_login_tokens()
        except requests.exceptions.HTTPError:
            raise LoginError(
                "Unable to log in. Check your credentials or authentication code and try again."
            )
        except requests.exceptions.ConnectionError:
            raise requests.exceptions.ConnectionError(
                "Failed to connect to robinhood. Please check your internet and try again."
            )

    def _generate_payload_for_login(self):
        self.payload = {
            "username": self.credentials[0],
            "password": self.credentials[1],
            "grant_type": "password",
            "client_id": self.client_id,
            "scope": "internal",
            "device_token": self.device_token,
        }

        if self.qr_code:
            multi_factor_auth_token = self._generate_multi_factor_auth_token()
            self.payload.update({"mfa_code": multi_factor_auth_token})
        elif self.manual_code:
            self.payload.update({"mfa_code": self.manual_code})

    def _generate_multi_factor_auth_token(self, current_time_seed=None):
        if current_time_seed is None:
            current_time_seed = int(time.time()) // 30

        cstruct_seed = struct.pack(">Q", current_time_seed)
        cstruct_key = base64.b32decode(self.qr_code, True)
        hmac_object = hmac.new(cstruct_key, cstruct_seed, hashlib.sha1)
        hmac_digest = hmac_object.digest()
        auth_token = self._get_multi_factor_auth_token(hmac_digest)

        return auth_token

    def _get_multi_factor_auth_token(self, hmac_digest):
        start_position = hmac_digest[19] & 0b1111
        end_position = start_position + 4
        auth_token = struct.unpack(
            ">I", hmac_digest[start_position:end_position]
        )[0]
        auth_token &= 0x7FFFFFFF
        auth_token %= 1000000
        auth_token = f"{auth_token:06d}"

        return auth_token

    def _generate_payload_for_manual_challenge(self):
        self.payload = {
            "username": self.credentials[0],
            "password": self.credentials[1],
            "grant_type": "password",
            "client_id": self.client_id,
            "expires_in": "86400",
            "scope": "internal",
            "device_token": self.device_token,
            "challenge_type": "sms",
        }

    def _perform_manual_challenge(self):
        endpoint = api.token()
        self.post(endpoint, data=self.payload, timeout=15)
        self.manual_code = input("Type in code from SMS or Authenticator app: ")

    def _extract_login_tokens(self):
        data_has_access_token = "access_token" in self.login_data.keys()
        data_has_refresh_token = "refresh_token" in self.login_data.keys()

        if data_has_access_token and data_has_refresh_token:
            self.site_auth_token = self.login_data["access_token"]
            self.refresh_token = self.login_data["refresh_token"]
            self.headers["Authorization"] = f"Bearer {self.site_auth_token}"
            self.is_logged_in = True
        else:
            raise LoginError(
                "Data returned from Robinhood does not contain 'access_token' or 'refresh_token'."
            )

    def _clear_credentials(self):
        self.credentials = (None, None)
        self.qr_code = None
        self.manual_code = None
        self.login_data = None

    def _clear_session_info(self):
        self.headers["Authorization"] = None
        self.site_auth_token = None
        self.is_logged_in = False
        self.account_numbers = None

