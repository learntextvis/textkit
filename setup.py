#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys
from setuptools import setup, find_packages


def find_version(fname):
    """Attempts to find the version number in the file names fname.
    Raises RuntimeError if not found.
    """
    version = ''
    with open(fname, 'r') as fp:
        reg = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
        for line in fp:
            m = reg.match(line)
            if m:
                version = m.group(1)
                break
    if not version:
        raise RuntimeError('Cannot find version information')
    return version

__version__ = find_version("textkit/__init__.py")


setup(
    name='textkit',
    version=__version__,
    description='Simple text analysis from the command line',
    long_description=open("README.rst").read(),
    packages=find_packages(exclude=['test*', 'docs']),
    license='MIT',
    author='Learn Text Vis Team',
    author_email='landham@gmail.com',
    py_modules=['textkit'],
    url='https://github.com/learntextvis/textkit',
    keywords=['text', 'analysis', 'textkit'],
    include_package_data=True,
    install_requires=[
        'click>=6.2',
        'nltk>=3.1'
    ],
    entry_points={
     'console_scripts': [
        'textkit = textkit.cli:cli'
     ]
    },
    package_data={
        'textkit': ['data/stopwords/english.txt', 'data/stopwords/german.txt']
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Topic :: Utilities'
    ]
)
