# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

import os
import sys

from setuptools import setup, find_packages

VERSION = '0.2.4'

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a v%s -m 'version %s'" % (VERSION, VERSION))
    print("  git push --tags")
    sys.exit()

setup(
    name='django-zeropush-reflux',
    version=VERSION,
    author='Saurabh Kumar',
    author_email='me@saurabh-kumar.com',
    packages=find_packages(exclude=['*tests*']),
    include_package_data=False,
    install_requires=[
        'requests'
    ],
    url='https://github.com/theskumar/django-zeropush-reflux',
    license='BSD licence, see LICENCE.txt',
    description='ZeroPush iOS push notifications support for django',

    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
