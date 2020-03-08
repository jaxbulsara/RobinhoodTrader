from __future__ import absolute_import

import requests


class HTTPDataMixin:
    self: requests.Session

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
