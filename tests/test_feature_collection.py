"""Test the geestac catalog module."""

import ee

from geestac import eecatalog

fao = eecatalog.FAO().GAUL_2015_level0()


class TestFeatureCollection:
    """Test an optical EO ImageCollection."""

    def test_ee_type(self):
        """Test an optical earth observation ImageCollection."""
        assert fao.eeType == ee.FeatureCollection

    def test_properties(self):
        """Test properties."""
        assert fao.properties.as_list("name") == [
            "ADM0_CODE",
            "ADM0_NAME",
            "DISP_AREA",
            "STATUS",
            "Shape_Area",
            "Shape_Leng",
            "EXP0_YEAR",
            "STR0_YEAR",
        ]
