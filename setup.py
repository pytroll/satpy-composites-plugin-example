#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) Satpy developers
"""Setup."""

from setuptools import setup
import os

setup(
    name='satpy-cpe',
    entry_points={
        'satpy.composites': [
            'example_composites = satpy_cpe',
        ],
    },
    package_data={'satpy_cpe': [os.path.join('etc', 'composites/*.yaml')]},
    install_requires=["satpy"],
    python_require=">=3.8",
)
