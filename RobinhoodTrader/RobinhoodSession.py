from __future__ import absolute_import
from .exceptions import CredentialError, LoginError
from .wrappers import auth_required
from .endpoints import api
from .config import get_qr_code

import requests, platform, sys, uuid, time, struct, base64, hmac, hashlib
from getpass import getpass
from urllib.request import getproxies


class RobinhoodSession(requests.Session):
    def __init__(self):
        super(RobinhoodSession, self).__init__()
        self.proxies = getproxies()
        self.device_token = str(uuid.uuid4())
        self.client_id = "c82SH0WZOsabOXGP2sxqcj34FxkvfnWRZBKlBjFS"
        self.credentials = (None, None)
        self.site_auth_token = None
        self.refresh_token = None
        self.headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en;q=1, fr;q=0.9, de;q=0.8, ja;q=0.7, nl;q=0.6, it;q=0.5",
            "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
            "X-Robinhood-API-Version": "1.0.0",
            "Connection": "keep-alive",
            "User-Agent": "Robinhood/823 (iPhone; iOS 7.1.2; Scale/2.00)",
        }
        self.is_logged_in = False
        self.session_is_console = sys.stdout.isatty()
        self.account_numbers = None

    def login(self, credentials=(None, None)):
        if None in credentials:
            if self.session_is_console:
                credentials = self._get_credentials_from_user()
            else:
                raise ValueError(
                    "This method is not being called in an interactive console. Must pass a non-null tuple of credentials."
                )

        if None in credentials:
            print("Login cancelled.")

        else:
            self.credentials = credentials
            qr_code = get_qr_code()
            payload = self._generate_payload(credentials, qr_code=qr_code)
            self._get_access_token(payload, qr_code)
            self._get_account_numbers()

    def logout(self):
        endpoint = api.revoke_token()
        payload = {
            "client_id": self.client_id,
            "token": self.refresh_token,
        }

        logout_request = self.post(endpoint, data=payload, timeout=15)
        logout_request.raise_for_status()

        self._clear_session_info()

    def get_data(self, *args, **kwargs):
        response = self.get(*args, **kwargs)
        response.raise_for_status()
        data = response.json()
        return data

    def head_data(self, *args, **kwargs):
        response = self.head(*args, **kwargs)
        response.raise_for_status()
        data = response.json()
        return data

    def post_data(self, *args, **kwargs):
        response = self.post(*args, **kwargs)
        response.raise_for_status()
        data = response.json()
        return data

    def put_data(self, *args, **kwargs):
        response = self.put(*args, **kwargs)
        response.raise_for_status()
        data = response.json()
        return data

    def delete_data(self, *args, **kwargs):
        response = self.delete(*args, **kwargs)
        response.raise_for_status()
        data = response.json()
        return data

    def options_data(self, *args, **kwargs):
        response = self.options(*args, **kwargs)
        response.raise_for_status()
        data = response.json()
        return data

    def patch_data(self, *args, **kwargs):
        response = self.patch(*args, **kwargs)
        response.raise_for_status()
        data = response.json()
        return data

    def _get_credentials_from_user(self):
        print("Press Enter to cancel.")
        username = input("Username: ")
        if username != "":
            password = getpass(prompt="Password: ")
        else:
            password = None

        return (username, password)

    def _generate_payload(self, credentials, qr_code=None, manual_code=None):
        if qr_code or manual_code:
            payload = self._generate_payload_for_login(
                credentials, qr_code, manual_code
            )
        else:
            payload = self._generate_payload_for_manual_challenge(credentials)
            manual_code = self._perform_manual_challenge(payload)
            payload = self._generate_payload_for_login(
                credentials, qr_code, manual_code
            )

        return payload

    def _get_access_token(self, payload, qr_code):
        try:
            login_data = self.post_data(api.token(), data=payload, timeout=15)
            self._extract_login_tokens(login_data)
        except requests.exceptions.HTTPError:
            print(f"Failed to login.")
            raise LoginError()
        except requests.exceptions.ConnectionError:
            print(
                f"Failed to connect. Please check your internet and try again."
            )

    def _generate_payload_for_login(
        self, credentials, qr_code=None, manual_code=None
    ):
        payload = {
            "username": credentials[0],
            "password": credentials[1],
            "grant_type": "password",
            "client_id": self.client_id,
            "scope": "internal",
            "device_token": self.device_token,
        }

        if qr_code:
            multi_factor_auth_token = self._generate_multi_factor_auth_token(
                qr_code
            )
            payload["mfa_code"] = multi_factor_auth_token
        elif manual_code:
            payload["mfa_code"] = manual_code

        return payload

    def _generate_multi_factor_auth_token(
        self, qr_code, current_time_seed=None
    ):
        if current_time_seed is None:
            current_time_seed = int(time.time()) // 30

        cstruct_seed = struct.pack(">Q", current_time_seed)
        cstruct_key = base64.b32decode(qr_code, True)
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

    def _generate_payload_for_manual_challenge(self, credentials):
        payload = {
            "username": credentials[0],
            "password": credentials[1],
            "grant_type": "password",
            "client_id": self.client_id,
            "expires_in": "86400",
            "scope": "internal",
            "device_token": self.device_token,
            "challenge_type": "sms",
        }

        return payload

    def _perform_manual_challenge(self, payload):
        endpoint = api.token()
        self.post(endpoint, data=payload, timeout=15)
        manual_code = input("Type in code from SMS or Authenticator app: ")
        return manual_code

    def _extract_login_tokens(self, login_data):
        data_has_access_token = "access_token" in login_data.keys()
        data_has_refresh_token = "refresh_token" in login_data.keys()

        if data_has_access_token and data_has_refresh_token:
            self.site_auth_token = login_data["access_token"]
            self.refresh_token = login_data["refresh_token"]
            self.headers["Authorization"] = f"Bearer {self.site_auth_token}"
            self.is_logged_in = True
        else:
            print(
                "Unable to login. Please enter different credentials and try again."
            )
            self.login()

    @auth_required
    def _get_account_numbers(self):
        endpoint = api.accounts()
        data = self.get_data(endpoint, timeout=15)
        self.account_numbers = list(
            map(lambda account: account["account_number"], data["results"],)
        )
        return self.account_numbers

    def _clear_session_info(self):
        self.headers["Authorization"] = None
        self.site_auth_token = None
        self.is_logged_in = False
        self.account_numbers = None
