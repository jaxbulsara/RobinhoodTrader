from __future__ import absolute_import

from .mixins import AuthenticationMixin, DataWrapperMixin


class RobinhoodSession(AuthenticationMixin, DataWrapperMixin):
    pass
