#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
setuptools config file
"""

import sys
import pip
from pip.req import parse_requirements
from setuptools import setup, find_packages
import os
from snaplayer import __version__ as version
from snaplayer import __author__ as author
from snaplayer import PKG_URL as pkg_url
from snaplayer import __name__ as pkg_name


# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements('requirements.txt', session=pip.download.PipSession())

# reqs is a list of requirement
# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name=pkg_name,
    version=version,
    packages=find_packages(),
    author=author,
    author_email="alejandroricoveri@gmail.com",
    description="Make images out of your Softlayer virtual servers, painlessly",
    long_description=open('README.rst').read(),
    url=pkg_url,
    license='MIT',
    download_url="{url}/tarball/{version}".format(url=pkg_url, version=version),
    keywords=['softlayer', 'backup'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console	',
        'Topic :: System :: Archiving :: Backup',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.3',
    ],
    entry_points={
        'console_scripts': [
            'snaplayer = snaplayer.__main__:main',
        ],
    },
    install_requires = reqs,
)
