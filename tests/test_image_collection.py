"""Test the geestac catalog module."""

import ee

import geestac


class TestOpticalImageCollection:
    """Test an optical EO ImageCollection."""

    l9 = geestac.ImageCollection(
        "https://storage.googleapis.com/earthengine-stac/catalog/LANDSAT/LANDSAT_LC09_C02_T2.json"
    )

    def test_ee_type(self):
        """Test an optical earth observation ImageCollection."""
        assert self.l9.eeType == ee.ImageCollection
