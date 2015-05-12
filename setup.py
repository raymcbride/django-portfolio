#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages

setup(
    name="django-portfolio",
    version="0.0.1",
    author="Ray McBride",
    author_email="ray@raymcbride.com",
    description=("Simple portfolio app"),
    license="BSD",
    url="https://bitbucket.org/raymcbride/django-portfolio",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 1 - Planning",
        'Environment :: Web Environment',
        'Framework :: Django',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "License :: OSI Approved :: BSD License",
    ],
)
