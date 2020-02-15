class RobinhoodException(Exception):
    pass


class LoginFailed(RobinhoodException):
    pass


class InvalidLogin(LoginFailed):
    pass
