"""Test the geestac catalog module."""

from geestac import eecatalog, fromId

cop = eecatalog.COPERNICUS()


class TestEECatalog:
    """Test EECatalog."""

    def test_data(self):
        """Test eecatalog data."""
        assert cop.name == "COPERNICUS"
        assert isinstance(cop.data, dict)

    def test_children(self):
        """Test catalog children."""
        children = cop.children.as_list("name")
        assert children == [
            "CORINE_V18_5_1_100m",
            "CORINE_V20_100m",
            "Landcover_100m_Proba_V_C3_Global",
            "Landcover_100m_Proba_V_Global",
            "S1_GRD",
            "S2",
            "S2_HARMONIZED",
            "S2_CLOUD_PROBABILITY",
            "S2_SR",
            "S2_SR_HARMONIZED",
            "S3_OLCI",
            "S5P_NRTI_L3_AER_AI",
            "S5P_NRTI_L3_AER_LH",
            "S5P_NRTI_L3_CLOUD",
            "S5P_NRTI_L3_CO",
            "S5P_NRTI_L3_HCHO",
            "S5P_NRTI_L3_NO2",
            "S5P_NRTI_L3_O3",
            "S5P_NRTI_L3_SO2",
            "S5P_OFFL_L3_AER_AI",
            "S5P_OFFL_L3_AER_LH",
            "S5P_OFFL_L3_CH4",
            "S5P_OFFL_L3_CLOUD",
            "S5P_OFFL_L3_CO",
            "S5P_OFFL_L3_HCHO",
            "S5P_OFFL_L3_NO2",
            "S5P_OFFL_L3_O3",
            "S5P_OFFL_L3_O3_TCL",
            "S5P_OFFL_L3_SO2",
            "DEM_GLO30",
        ]

    def test_parent(self):
        """Test parent."""
        assert cop.parent == eecatalog

    def test_from_id_catalog(self):
        """Test fromId (catalog)."""
        assert fromId("COPERNICUS") == cop

    def test_from_id_dataset(self):
        """Test fromId (dataaset)."""
        assert fromId("COPERNICUS/S2_SR_HARMONIZED") == cop.S2_SR_HARMONIZED()
        assert fromId("LANDSAT/LC09/C02/T1") == eecatalog.LANDSAT.LC09_C02_T1()
