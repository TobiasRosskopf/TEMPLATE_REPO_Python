#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-

"""
**Created:**    ??.??.2022
**Modified:**   ??.??.2022

**Authors:**    [Tobias Rosskopf](mailto:tobirosskopf@gmail.com)

Setup file for the package
"""

# from setuptools import setup
from setuptools import find_packages

from distutils.core import setup
# from distutils.core import find_packages

from package_name import (
    __name__,
    __version__,
    __description__,
    __author__,
    __email__,
    __license__,
)


PACKAGE_LIST = [
    __name__,
]


with open("README.md", "r") as file_readme:
    README = file_readme.read()

with open("HISTORY.md", "r") as file_history:
    HISTORY = file_history.read()

with open("requirements.txt") as file_requirements:
    REQUIREMENTS = [req.strip() for req in file_requirements.readlines() if "==" in req]

with open("requirements-dev.txt") as file_requirements_dev:
    REQUIREMENTS_DEV = [req.strip() for req in file_requirements_dev.readlines() if "==" in req]


setup(
    # Metadata
    name=__name__,
    version=__version__,
    description=__description__,
    long_description=f"{README}\n{HISTORY}",
    long_description_content_type='text/markdown',
    license=__license__,
    author=__author__,
    author_email=__email__,
    url=f"https://github.com/tobiasrosskopf/{__name__}",
    keywords="",

    # Package info
    python_requires=">=3.9",
    packages=find_packages(include=PACKAGE_LIST),
    install_requires=REQUIREMENTS,
    include_package_data=True,
    entry_points={
        "console_scripts": [
            f"{__name__}={__name__}.cli:main",
        ],
    },

    # Tests
    test_suite="tests",
    tests_require=REQUIREMENTS_DEV,
)
