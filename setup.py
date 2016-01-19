#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='textkit',
    packages=['textkit'],
    version='0.0.1',
    py_modules=['textkit'],
    url='https://github.com/learntextvis/textkit',
    keywords=['text', 'analysis', 'textkit'],
    install_requires=[
        'click>=6.2',
        'nltk>=3.1'
    ],
    entry_points={
     'console_scripts': [
        'textkit = textkit.cli:cli'
     ]
    }
)
