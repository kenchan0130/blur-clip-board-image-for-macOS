#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="blur-clip-board-image-cli",
    url='https://github.com/kenchan0130/blur-clip-board-image-for-macOS',
    version="0.0.1",
    description="Blur clip board image command line tool for macOS",
    author="Tadayuki Onishi",
    packages=find_packages("."),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "blur-clip-board-image=app:main"
        ]
    },
    license="MIT"
)