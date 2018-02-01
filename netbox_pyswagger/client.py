
from requests import Session
from halutz.client import Client as HalutzClient

__all__ = ['Client']


class Client(HalutzClient):
    apidocs_url = "/api/docs?format=openapi"

    def __init__(self, api_token, **halutz_kwargs):
        # the api version will get set when the spec is loaded from the server
        self.api_version = None

        kwargs = halutz_kwargs or {}

        if 'session' not in kwargs:
            kwargs['session'] = Session()

        # setup the token in the session headers
        kwargs['session'].headers['Authorization'] = "Token %s" % api_token

        # invoke the halutz initializer
        super(Client, self).__init__(**kwargs)

    @classmethod
    def from_pynetbox(cls, pynb):
        kwargs = dict()
        kwargs['api_token'] = pynb.api_kwargs['token']
        kwargs['server_url'] = pynb.api_kwargs['base_url'].split('/api')[0]
        kwargs['remote'] = pynb

        return cls(**kwargs)

    def fetch_swagger_spec(self):
        url = "%s%s" % (self.server_url, self.apidocs_url)
        resp = self.session.get(url)

        if not resp.ok:
            raise RuntimeError(
                'unable to fetch Swagger spec:', resp)

        spec = resp.json()
        if 'paths' not in spec:
            if spec.get('details', '') == 'Invalid token':
                raise RuntimeError('Invalid API token provided')

        self.api_version = resp.headers['API-Version']

        if self.api_version == "2.2":
            from .patch_2_2 import patch_spec
            patch_spec(spec)

        return spec
