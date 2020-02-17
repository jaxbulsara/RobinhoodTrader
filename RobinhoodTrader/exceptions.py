import requests


class RobinhoodException(Exception):
    pass


class CredentialError(RobinhoodException):
    pass


class LoginError(RobinhoodException):
    pass

