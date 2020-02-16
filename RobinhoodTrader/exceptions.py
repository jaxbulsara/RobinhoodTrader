class RobinhoodException(Exception):
    pass


class CredentialError(RobinhoodException):
    pass


class LoginFailed(RobinhoodException):
    pass
