#!/usr/bin/env python

import sys
exec(open('bakeit/version.py').read())
assert sys.version >= '2.6', "Requires Python v2.6 or above."
from setuptools import setup

classifiers = [
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2.5",
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3.2",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

install_requires = ["requests", "requests[security]", "pyperclip"]
tests_require = ["pep8", "pytest"] + install_requires


setup(
    name="bakeit",
    version=__version__,  # noqa
    author="Stavros Korokithakis",
    author_email="hi@stavros.io",
    url="https://github.com/skorokithakis/bakeit/",
    description="A command-line interface for Pastery, the best"
                " pastebin in the world.",
    long_description=open("README.rst").read(),
    license="MIT",
    classifiers=classifiers,
    packages=["bakeit"],
    install_requires=install_requires,
    tests_require=tests_require,
    test_suite='bakeit.tests',
    entry_points={
        'console_scripts': ['bakeit=bakeit.cli:main'],
    },
)
