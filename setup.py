#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pip.req import parse_requirements
from setuptools import setup, find_packages

requirements = [str(r.req) for r in parse_requirements('requirements.txt')]

setup(
    name='django-portfolio',
    version='0.0.1',
    author='Ray McBride',
    author_email='ray@raymcbride.com',
    description='Simple portfolio app',
    license='BSD',
    url='https://github.com/raymcbride/django-portfolio',
    install_requires=[requirements],
    packages=find_packages(),
    classifiers=[
        "Development Status :: 1 - Planning",
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        "License :: OSI Approved :: BSD License",
    ],
)
