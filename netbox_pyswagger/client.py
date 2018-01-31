
from requests import Session
from halutz.client import Client as HalutzClient

__all__ = ['Client']


class Client(HalutzClient):
    apidocs_url = "/api/docs?format=openapi"

    def __init__(self, server_url, api_token, session=None, remote=None):
        netbox = session or Session()
        netbox.headers['Authorization'] = "Token %s" % api_token

        super(Client, self).__init__(
            server_url=server_url,
            session=netbox,
            remote=remote)

    @classmethod
    def from_pynetbox(cls, pynb):
        api_token = pynb.api_kwargs['token']
        server_url = pynb.api_kwargs['base_url'].split('/api')[0]

        return cls(server_url=server_url,
                   api_token=api_token,
                   remote=pynb)

    def fetch_swagger_spec(self):
        url = "%s%s" % (self.server_url, self.apidocs_url)
        return self.session.get(url).json()
