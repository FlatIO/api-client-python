# coding: utf-8

"""
    Flat API 2.17.0

    OpenAPI spec version: 
    Contact: developers@flat.io
"""


import sys
from setuptools import setup, find_packages

NAME = "flat_api"
VERSION = "0.8.1"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

try:
    import pypandoc
    LONG_DESCRIPTION = open('README.md').read()
    LONG_DESCRIPTION = LONG_DESCRIPTION[:LONG_DESCRIPTION.index('## Documentation for API Endpoints')]
    LONG_DESCRIPTION = pypandoc.convert_text(LONG_DESCRIPTION, 'rst', format='md')
except(IOError, ImportError):
    LONG_DESCRIPTION = open('README.md').read()

setup(
    name=NAME,
    version=VERSION,
    description="Flat API Client",
    author="The Flat Team (https://flat.io)",
    author_email="developers@flat.io",
    url="https://github.com/FlatIO/api-client-python",
    keywords=["Flat API", "MusicXML", "Music Notation", "MIDI"],
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    install_requires=REQUIRES,
    packages=find_packages(exclude=['test']),
    include_package_data=True,
    license="Apache",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Artistic Software",
        "Topic :: Education",
        "Topic :: Multimedia :: Sound/Audio"
    ]
)
