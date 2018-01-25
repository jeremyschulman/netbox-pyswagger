# Python Swagger Client for Netbox

If you love [Netbox](https://github.com/digitalocean/netbox), and you 
want to automate the server via its REST API, then this package is for you.
If you are already using the [pynetbox](https://github.com/digitalocean/pynetbox)
client you can use both together.

The `netbox-pyswagger` client consumes the Netbox Swagger 2.0 spec
from the server and provides you "user-friendly" programming
model that:

  - Does not require you to know any specific APIs.
  - Validates all of your inputs based on the spec json-schemas
  - Provides object models for all parameter body data structures so
  you can create body data that is validated as you go along
  - Provides introspection "help" information, if you are using an
  interactive interpreter environment such as ipython and jupyter notebooks

The `netbox-pyswagger` client is built on the [halutz](https://github.com/jeremyschulman/halutz) library.  
For detailed examples and usage,
 please refer to the halutz [tutorials](https://github.com/jeremyschulman/halutz/tree/master/docs)
 
# Installation

```bash
pip install netbox-pyswagger
```

# Example

The following example uses the Netbox URL and token from
some environment variables, and creates the netbox-pyswagger
instance, and gets all of the VLANs.

```python
import os
import sys

from netbox_pyswagger import Client

base_url = os.getenv('NETBOX_SERVER')
if not base_url:
    sys.exit('NETBOX_SERVER not found in enviornment')

netbox_token = os.getenv('NETBOX_TOKEN')
if not netbox_token:
    sys.exit('NETBOX_TOKEN not found in environment')

netbox = Client(base_url=base_url, api_token=netbox_token)

# Run the command to get all VLANs.  Note the first attribute
# after request is the Swagger tag value (ipam), and the final attribute
# is the operationId value (ipam_vlans_list).

resp, ok = netbox.request.ipam.ipam_vlans_list()
```

The `resp` contains the response payload, for example:

```json
{
  "count": 2, 
  "previous": null, 
  "results": [
    {
      "status": {
        "value": 1, 
        "label": "Active"
      }, 
      "group": null, 
      "name": "green", 
      "vid": 99, 
      "site": null, 
      "role": null, 
      "custom_fields": {}, 
      "display_name": "99 (green)", 
      "id": 4, 
      "tenant": null, 
      "description": ""
    }, 
    {
      "status": {
        "value": 1, 
        "label": "Active"
      }, 
      "group": null, 
      "name": "Blue", 
      "vid": 100, 
      "site": null, 
      "role": null, 
      "custom_fields": {}, 
      "display_name": "100 (Blue)", 
      "id": 3, 
      "tenant": null, 
      "description": ""
    }
  ], 
  "next": null
}
```


# Example - with pynetbox

Here is the same example of using netbox-pyswagger and pynetbox
client.  When you use this approach, the netbox-pyswagger instance
maintains an attribute called `remote` which is set to the pynetbox
instance you provided.

```python
import os
import sys

import pynetbox
from netbox_pyswagger import Client

base_url = os.getenv('NETBOX_SERVER')
if not base_url:
    sys.exit('NETBOX_SERVER not found in enviornment')

netbox_token = os.getenv('NETBOX_TOKEN')
if not netbox_token:
    sys.exit('NETBOX_TOKEN not found in environment')

# create the netbox-pyswagger instance, passing in the
# pynetbox client instance

netbox = Client(pynb=pynetbox.api(url=base_url, token=netbox_token))

# run the command to get all VLANs using the pynetbox method

resp = netbox.remote.ipam.vlans.all()
```

The `resp` contains the pynetbox VLAN instance values.  For the
same example, `resp` would contain the list `[green, blue]`.
For example, dumping out the *green* instance:

```python
for name, value in resp[0]:
    print(name, value)
```

results in:
```bash
status {u'value': 1, u'label': u'Active'}
group None
name green
vid 99
site None
role None
tenant None
display_name 99 (green)
id 4
custom_fields {}
description 
```

