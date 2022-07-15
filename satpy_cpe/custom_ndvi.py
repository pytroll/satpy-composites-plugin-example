#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2015-2022 Satpy developers
"""Some example compositor."""

from satpy.composites import GenericCompositor
from satpy.dataset import combine_metadata


class NDVICompositor(GenericCompositor):
    """NDVI compositor."""

    def __call__(self, projectables, **kwargs):
        """Generate the ndvi."""
        # Check that the datasets match
        projectables = self.match_data_arrays(projectables)

        vis06, vis08 = projectables
        ndvi = (vis08 - vis06) / (vis08 + vis06)
        ndvi.attrs = combine_metadata(vis08, vis06)

        return super(NDVICompositor, self).__call__([ndvi], **kwargs)
