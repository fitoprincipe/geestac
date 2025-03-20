"""Test the geestac catalog module."""

import ee

import geestac


class TestFeatureCollection:
    """Test an optical EO ImageCollection."""

    fao = geestac.FeatureCollection(
        "https://storage.googleapis.com/earthengine-stac/catalog/FAO/FAO_GAUL_2015_level0.json"
    )

    def test_ee_type(self):
        """Test an optical earth observation ImageCollection."""
        assert self.fao.eeType == ee.FeatureCollection
