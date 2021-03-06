#!/usr/bin/env python

from distutils.core import setup
from setuptools import setup, Command, find_packages

DISTNAME = 'dx'

setup(name=DISTNAME,
		version='0.1',
                packages=find_packages(include=['dx', 'dx.*']),
		description='DX Analytics',
		author='Dr. Yves Hilpisch',
		author_email='dx@tpq.io',
		url='http://dx-analytics.com/')
