
def patch_spec(spec):
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
