from __future__ import print_function

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


pynb = pynetbox.api(url=base_url, token=netbox_token)
netbox = Client(pynb=pynb)
