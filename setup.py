#! /usr/bin/env python

from setuptools import setup

setup(
    name                 = 'qless-util',
    version              = '0.1.1',
    description          = 'Qless utilities',
    long_description     = '''Utilities for qless.''',
    url                  = 'http://github.com/seomoz/qless-util-py',
    author               = 'Dan Lecocq',
    author_email         = 'dan@moz.com',
    license              = "MIT License",
    keywords             = 'redis, qless, job',
    packages             = [
        'qless_util',
        'qless_util.jobs'
    ],
    package_dir          = {
        'qless_util': 'qless_util',
        'qless_util.jobs': 'qless_util/jobs'
    },
    install_requires     = [
        'decorator',
        'hiredis',
        'qless-py>=0.11.4',
        'redis',
        'six',
        'simplejson'
    ],
    tests_requires       = [
        'coverage',
        'mock',
        'nose',
        'rednose',
        'setuptools>=17.1'
    ],
    classifiers          = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent'
    ]
)
