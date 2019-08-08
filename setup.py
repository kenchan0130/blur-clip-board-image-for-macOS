#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="blur-clip-board-image-cli",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
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