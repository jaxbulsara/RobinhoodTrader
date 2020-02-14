class RobinhoodException(Exception):
    pass


class LoginFailed(RobinhoodException):
    pass


class LoginResponseError(LoginFailed):
    pass
