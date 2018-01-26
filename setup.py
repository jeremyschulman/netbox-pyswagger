#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
import netbox_pyswagger


def read(fname):
    with open(fname) as fp:
        content = fp.read()
    return content


setup(
    name='netbox-pyswagger',
    version=netbox_pyswagger.__version__,
    description='Swagger client for Netbox',
    author='Jeremy Schulman',
    author_email='nwkautomaniac@gmail.com',
    url='https://github.com/jeremyschulman/netbox-pyswagger',
    packages=['netbox_pyswagger'],
    license='MIT',
    zip_safe=False,
    install_requires=[
        'halutz>=0.2.0',
        'requests',
        'six'
    ],
    keywords=('netbox', 'rest', 'json', 'api',
              'network', 'automation'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ]
)
