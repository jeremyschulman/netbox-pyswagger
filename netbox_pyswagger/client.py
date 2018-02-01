
from requests import Session
from halutz.client import Client as HalutzClient

__all__ = ['Client']


class Client(HalutzClient):
    apidocs_url = "/api/docs?format=openapi"

    def __init__(self, server_url, api_token, session=None, remote=None):
        netbox = session or Session()
        netbox.headers['Authorization'] = "Token %s" % api_token
        self.api_version = None

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
        resp = self.session.get(url)

        if not resp.ok:
            raise RuntimeError(
                'unable to fetch Swagger spec:', resp)

        spec = resp.json()
        if 'paths' not in spec:
            if spec.get('details', '') == 'Invalid token':
                raise RuntimeError('Invalid API token provided')

        self.api_version = resp.headers['API-Version']

        # Fix for Netbox #1853 https://github.com/digitalocean/netbox/issues/1853
        for path in spec['paths'].keys():
            for method in spec['paths'][path].keys():

                if 'parameters' not in spec['paths'][path][method].keys():
                    continue

                for param in spec['paths'][path][method]['parameters']:
                    if param['in'] != 'body':
                        continue
                    
                    if 'custom_fields' not in param['schema']['properties'].keys():
                        continue
                
                    if param['schema']['properties']['custom_fields']['type'] == 'string':
                        param['schema']['properties']['custom_fields']['type'] = 'object'
                    
        return spec
