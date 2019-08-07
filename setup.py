#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('requirements.txt') as requirements_file:
    install_requirements = requirements_file.read().splitlines()

setup(
    name="blur-clip-board-image-cli",
    version="0.0.1",
    description="Blur clip board image command line tool for macOS",
    author="karakaram",
    install_requires=install_requirements,
    entry_points={
        "console_scripts": [
            "blur-clip-board-image = app:main"
        ]
    },
    license="MIT"
)