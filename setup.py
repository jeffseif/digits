#! /usr/bin/env python3
from setuptools import setup
from digits import __author__
from digits import __description__
from digits import __email__
from digits import __program__
from digits import __url__
from digits import __version__


setup(
    author=__author__,
    author_email=__email__,
    description=__description__,
    install_requires=[
        'numpy>=1.11.3',
        'Pillow>=3.4.2',
        'scikit-learn>=0.18.1',
        'scipy>=0.18.1',
    ],
    name=__program__,
    packages=[__program__],
    platforms='all',
    setup_requires=[
        'setuptools',
        'tox',
    ],
    test_suite='tests',
    url=__url__,
    version=__version__,
)
