#!/usr/bin/env python

from distutils.core import setup

setup(name='algebra',
    version='1.0',
    description='A small algebra manuplation packge',
    author='Mehtap Isik',
    author_email='mehtap.isik@choderalab.org',
    url='',
    enrty_points = {'console_scripts': ['algebra-product=algebra.cli:main']}
    )
