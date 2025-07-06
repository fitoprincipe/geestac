"""Test the geestac catalog module."""

import ee

from geestac import eecatalog


class TestImage:
    """Test an optical EO ImageCollection."""

    srtm = eecatalog.CGIAR().SRTM90_V4()

    def test_ee_type(self):
        """Test an optical earth observation ImageCollection."""
        assert self.srtm.eeType == ee.Image

    def test_get_band_with_name(self):
        """Test getting a band using its name."""
        band = self.srtm.bands["elevation"]
        assert band.name == "elevation"
