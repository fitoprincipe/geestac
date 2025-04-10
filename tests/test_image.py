"""Test the geestac catalog module."""

import ee

from geestac import eecatalog


class TestImage:
    """Test an optical EO ImageCollection."""

    srtm = eecatalog.CGIAR().SRTM90_V4()

    def test_ee_type(self):
        """Test an optical earth observation ImageCollection."""
        assert self.srtm.eeType == ee.Image
