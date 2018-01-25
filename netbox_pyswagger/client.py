
from requests import Session
from halutz.client import Client as HalutzClient

__all__ = ['Client']


class Client(HalutzClient):
    apidocs_url = "/api/docs?format=openapi"

    def __init__(self, base_url=None, api_token=None, pynb=None):

        netbox = Session()

        if pynb:
            api_token = pynb.api_kwargs['token']
            base_url = pynb.api_kwargs['base_url'].split('/api')[0]
            netbox.headers['Authorization'] = "Token %s" % api_token
            super(Client, self).__init__(base_url=base_url,
                                         session=netbox, remote=pynb)
            return

        # not given instnace of pynetbox
        if not api_token:
            raise ValueError("api_token required")

        if not base_url:
            raise ValueError('base_url required')

        netbox.headers['Authorization'] = "Token %s" % api_token
        super(Client, self).__init__(
            base_url=base_url, session=netbox)

    def fetch_swagger_spec(self):
        url = "%s%s" % (self.base_url, self.apidocs_url)
        return self.session.get(url).json()
