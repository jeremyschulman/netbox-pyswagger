
from requests import Session
from halutz.client import Client as HalutzClient

__all__ = ['Client']


class Client(HalutzClient):
    apidocs_url = "/api/docs?format=openapi"

    def __init__(self, base_url, api_token):
        netbox = Session()
        netbox.headers['Authorization'] = "Token %s" % api_token
        super(Client, self).__init__(base_url=base_url, session=netbox)

    def fetch_swagger_spec(self):
        url = "%s%s" % (self.base_url, self.apidocs_url)
        return self.session.get(url).json()
