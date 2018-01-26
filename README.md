# Python Swagger Client for Netbox

If you love [Netbox](https://github.com/digitalocean/netbox), you want to automate it
via the REST API, and you want a client that supports an interactive enviornment like [ipython](https://ipython.org/)
and [jupyter notesbooks](http://jupyter.org/), then this client is for you!

The gist of this client is that it consumes the Netbox Swagger 2.0 spec and uses that information
to dynamically create a client with all API capabilities, model parameters as objects, and perform data validataton
on all request parameters and responses.  You never have to worry about the client being "out of sync"
with the Netbox API.  This client is specifically designed so that you can *introspect*, that is show in a "help" like manner,
everything about each API, parameter, and data-type so that you do not need to have any API docs.  You can use
this client in an interactive Python shell, such as ipython and jupyter notebooks, in order to create a *CLI-like* user
experience and not require **hard-core** programming to automate the Netbox system.  For these purpose, this
client was built with the halutz package - see these [tutorials](https://github.com/jeremyschulman/halutz/tree/master/docs)
for usage.

---
**NOTE:** &nbsp;&nbsp; If you are already using the <a href="https://github.com/digitalocean/pynetbox">pynetbox</a>
client you can use both together.  See this example [tutorial](examples/With-pynetbox-client.ipynb).  

---
 
# Installation

```bash
pip install netbox-pyswagger
```

# Quickstart

This example shows you how to create a client, and create a VLAN.
```python
from netbox_pyswagger.client import Client

server_url = "localhost:32768"
api_token = "0123456789abcdef0123456789abcdef01234567"

netbox = Client(server_url, api_token=api_token)

# Use the `request` attribute to access a specific API based on the Swagger tag value
# (ipam) and the Swagger operationId value (ipam_vlans_create)

new_vlan = netbox.request.ipam.ipam_vlans_create

# the command body parameter is called 'data' and here we set the required values
# if you set an invalid value, like setting `vid` to "foobaz", you will get a validation
# exception

new_vlan.data.vid = 10
new_vlan.data.name = 'Blue'

# finally execute the command, which provides us the response data and the indication
# if the command executed ok or not.  If the command had addition (non-body) parameters
# you would provide them as key-value pairs to the call.

resp, ok = new_vlan()
```

The variable `ok` is True when the command is successful, and here is the example output
of the response data, `resp`:

```json
{
  "status": 1, 
  "group": null, 
  "name": "Blue", 
  "vid": 10, 
  "site": null, 
  "role": null, 
  "id": 8, 
  "tenant": null, 
  "description": ""
}
```

## Built With

  - [bravado](https://github.com/Yelp/bravado) for consuming the Swagger spec
  - [jsonschemas](https://github.com/Julian/jsonschema) for validating Swagger json-schema
  - [python-jsonschema-objects](https://github.com/cwacek/python-jsonschema-objects) for classbuilding
  the json-schema objects
  - [halutz](https://github.com/jeremyschulman/halutz) for wrapping all the above together

## Other Links

  - [Swagger 2.0 Specification](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md)
  - [JSON-schema](http://json-schema.org/)

## Acknowledgements

The Netbox probject is quite amazing, with a vibrant community of users and contributors!  Many
thanks to [@jeremystretch](https://github.com/jeremystretch]) and [@digitalocean](https://github.com/digitalocean)!

## Questions / Contributes?

Please use the issues link to ask questions.  Contributions are welcome and apprecaited.