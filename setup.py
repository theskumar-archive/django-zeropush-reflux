# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from setuptools import find_packages, setup

setup(
    name='django-zeropush-2',
    version='0.2.3',
    author='Saurabh Kumar',
    author_email='me@saurabh-kumar.com',
    packages=find_packages(),
    url='https://github.com/theskumar/django-zeropush',
    license='BSD licence, see LICENCE.txt',
    description='ZeroPush iOS push notifications support for django',
    install_requires=['requests'],
    zip_safe=False,
)
