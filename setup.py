#!/bin/python
from setuptools import setup
setup(
    name='protozfitsreader',
    packages=['protozfitsreader'],
    version='0.44.1b0',
    description='Basic python bindings for protobuf zfits reader',
    author="Etienne Lyard et al.",
    author_email="etienne.lyard@unige.ch",
    package_data={
        'protozfitsreader': [
            '*.so*',
            '*.dylib'
        ],
        '': ['tests/resources/*'],
    },
    install_requires=['numpy', 'protobuf'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
