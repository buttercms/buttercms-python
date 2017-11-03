import requests

from .__version__ import __version__


class Client(object):
    """Client"""
    def __init__(self, auth_token):
        self.auth_token = auth_token
        self.url = 'https://api.buttercms.com/v2/'

    def api_get(self, slug='', params=None):
        payload = {
            'auth_token': self.auth_token,
        }
        if params:
            payload.update(params)

        headers = {
            'X-Butter-Client': 'Python/{}'.format(__version__),
        }

        response = requests.get(
            url=self.url + self.path + str(slug),
            params=payload,
            headers=headers,
        )
        return response.json()

    def get(self, slug='', params=None):
        return self.api_get(slug=slug, params=params)
