#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2015-2022 Satpy developers
"""Init module to define this directory as a python package.."""

# Convenience import of custom NDVICompositor so YAML configuration can
# use the shorter module name: satpy_cpe.NDVICompositor
from .custom_ndvi import NDVICompositor  # noqa
