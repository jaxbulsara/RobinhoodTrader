from __future__ import absolute_import
import requests
from . import exceptions


def auth_required(function):  # pylint: disable=E0213
    def make_user_login(self, *args, **kwargs):
        if type(self).__name__ == "RobinhoodSession":
            session = self
        else:
            session = self.session

        if not session.is_logged_in:
            session.login(session.credentials)
        return function(self, *args, **kwargs)  # pylint: disable=E1102

    return make_user_login
