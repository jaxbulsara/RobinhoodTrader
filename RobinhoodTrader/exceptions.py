from __future__ import absolute_import


class RobinhoodException(Exception):
    pass


class CredentialError(RobinhoodException):
    pass


class LoginError(RobinhoodException):
    pass


class RecordNotFoundError(RobinhoodException):
    pass


class CategoryError(RobinhoodException):
    pass


class IdentifierError(RobinhoodException):
    pass


class PageError(RobinhoodException):
    pass
