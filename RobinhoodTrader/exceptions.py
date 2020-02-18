from __future__ import absolute_import
import requests


class RobinhoodException(Exception):
    pass


class CredentialError(RobinhoodException):
    pass


class LoginError(RobinhoodException):
    pass

