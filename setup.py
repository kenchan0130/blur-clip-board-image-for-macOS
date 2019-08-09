#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name="blur-clip-board-image-cli",
    url='https://github.com/kenchan0130/blur-clip-board-image-for-macOS',
    version="0.0.4",
    description="Blur clip board image command line tool for macOS",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Tadayuki Onishi",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "blur-clip-board-image=blur_clip_board_image.app:main"
        ]
    },
    license="MIT"
)
