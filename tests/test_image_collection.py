"""Test the geestac catalog module."""

from types import SimpleNamespace

import ee

from geestac import eecatalog

l9 = eecatalog.LANDSAT().LC09_C02_T1()
s2 = eecatalog.COPERNICUS().S2_SR()


class TestOpticalImageCollection:
    """Test an optical EO ImageCollection."""

    def test_ee_type(self):
        """Test ee type."""
        assert l9.eeType == ee.ImageCollection

    def test_start_date(self):
        """Test start date."""
        assert l9.start_date == "2021-10-31T00:00:00Z"

    def test_status(self):
        """Test status."""
        assert s2.status == "deprecated"

    def test_asset_id(self):
        """Test AssetId."""
        assert s2.assetId == "COPERNICUS/S2_SR"

    def test_properties(self):
        """Test Properties."""
        properties = s2.properties.as_list("name")
        assert properties == [
            "AOT_RETRIEVAL_ACCURACY",
            "CLOUDY_PIXEL_PERCENTAGE",
            "CLOUD_COVERAGE_ASSESSMENT",
            "CLOUDY_SHADOW_PERCENTAGE",
            "DARK_FEATURES_PERCENTAGE",
            "DATASTRIP_ID",
            "DATATAKE_IDENTIFIER",
            "DATATAKE_TYPE",
            "DEGRADED_MSI_DATA_PERCENTAGE",
            "FORMAT_CORRECTNESS",
            "GENERAL_QUALITY",
            "GENERATION_TIME",
            "GEOMETRIC_QUALITY",
            "GRANULE_ID",
            "HIGH_PROBA_CLOUDS_PERCENTAGE",
            "MEAN_INCIDENCE_AZIMUTH_ANGLE_B1",
            "MEAN_INCIDENCE_AZIMUTH_ANGLE_B2",
            "MEAN_INCIDENCE_AZIMUTH_ANGLE_B3",
            "MEAN_INCIDENCE_AZIMUTH_ANGLE_B4",
            "MEAN_INCIDENCE_AZIMUTH_ANGLE_B5",
            "MEAN_INCIDENCE_AZIMUTH_ANGLE_B6",
            "MEAN_INCIDENCE_AZIMUTH_ANGLE_B7",
            "MEAN_INCIDENCE_AZIMUTH_ANGLE_B8",
            "MEAN_INCIDENCE_AZIMUTH_ANGLE_B8A",
            "MEAN_INCIDENCE_AZIMUTH_ANGLE_B9",
            "MEAN_INCIDENCE_AZIMUTH_ANGLE_B10",
            "MEAN_INCIDENCE_AZIMUTH_ANGLE_B11",
            "MEAN_INCIDENCE_AZIMUTH_ANGLE_B12",
            "MEAN_INCIDENCE_ZENITH_ANGLE_B1",
            "MEAN_INCIDENCE_ZENITH_ANGLE_B2",
            "MEAN_INCIDENCE_ZENITH_ANGLE_B3",
            "MEAN_INCIDENCE_ZENITH_ANGLE_B4",
            "MEAN_INCIDENCE_ZENITH_ANGLE_B5",
            "MEAN_INCIDENCE_ZENITH_ANGLE_B6",
            "MEAN_INCIDENCE_ZENITH_ANGLE_B7",
            "MEAN_INCIDENCE_ZENITH_ANGLE_B8",
            "MEAN_INCIDENCE_ZENITH_ANGLE_B8A",
            "MEAN_INCIDENCE_ZENITH_ANGLE_B9",
            "MEAN_INCIDENCE_ZENITH_ANGLE_B10",
            "MEAN_INCIDENCE_ZENITH_ANGLE_B11",
            "MEAN_INCIDENCE_ZENITH_ANGLE_B12",
            "MEAN_SOLAR_AZIMUTH_ANGLE",
            "MEAN_SOLAR_ZENITH_ANGLE",
            "MEDIUM_PROBA_CLOUDS_PERCENTAGE",
            "MGRS_TILE",
            "NODATA_PIXEL_PERCENTAGE",
            "NOT_VEGETATED_PERCENTAGE",
            "PROCESSING_BASELINE",
            "PRODUCT_ID",
            "RADIATIVE_TRANSFER_ACCURACY",
            "RADIOMETRIC_QUALITY",
            "REFLECTANCE_CONVERSION_CORRECTION",
            "SATURATED_DEFECTIVE_PIXEL_PERCENTAGE",
            "SENSING_ORBIT_DIRECTION",
            "SENSING_ORBIT_NUMBER",
            "SENSOR_QUALITY",
            "SOLAR_IRRADIANCE_B1",
            "SOLAR_IRRADIANCE_B2",
            "SOLAR_IRRADIANCE_B3",
            "SOLAR_IRRADIANCE_B4",
            "SOLAR_IRRADIANCE_B5",
            "SOLAR_IRRADIANCE_B6",
            "SOLAR_IRRADIANCE_B7",
            "SOLAR_IRRADIANCE_B8",
            "SOLAR_IRRADIANCE_B8A",
            "SOLAR_IRRADIANCE_B9",
            "SOLAR_IRRADIANCE_B10",
            "SOLAR_IRRADIANCE_B11",
            "SOLAR_IRRADIANCE_B12",
            "SNOW_ICE_PERCENTAGE",
            "SPACECRAFT_NAME",
            "THIN_CIRRUS_PERCENTAGE",
            "UNCLASSIFIED_PERCENTAGE",
            "VEGETATION_PERCENTAGE",
            "WATER_PERCENTAGE",
            "WATER_VAPOUR_RETRIEVAL_ACCURACY",
        ]

    def test_revisit(self):
        """Test revisit."""
        revisit = l9.revisit
        assert isinstance(revisit, SimpleNamespace)
        assert revisit.interval == 16
        assert revisit.unit == "day"


class TestBands:
    """Test bands."""

    def test_band_names(self):
        """Test band names."""
        names = s2.bands.as_list("name")
        assert names == [
            "B1",
            "B2",
            "B3",
            "B4",
            "B5",
            "B6",
            "B7",
            "B8",
            "B8A",
            "B9",
            "B11",
            "B12",
            "AOT",
            "WVP",
            "SCL",
            "TCI_R",
            "TCI_G",
            "TCI_B",
            "MSK_CLDPRB",
            "MSK_SNWPRB",
            "QA10",
            "QA20",
            "QA60",
            "MSK_CLASSI_OPAQUE",
            "MSK_CLASSI_CIRRUS",
            "MSK_CLASSI_SNOW_ICE",
        ]

    def test_band_scales(self):
        """Test band scales."""
        scales = l9.bands.as_dict("scale")
        assert scales == {
            "B1": 30,
            "B2": 30,
            "B3": 30,
            "B4": 30,
            "B5": 30,
            "B6": 30,
            "B7": 30,
            "B8": 15,
            "B9": 30,
            "B10": 30,
            "B11": 30,
            "QA_PIXEL": 30,
            "QA_RADSAT": 30,
            "SAA": 30,
            "SZA": 30,
            "VAA": 30,
            "VZA": 30,
        }

    def test_band_wavelength(self):
        """Test wavelength."""
        wavelength = s2.bands.as_dict("center_wavelength")
        assert wavelength == {
            "B1": 0.4439,
            "B2": 0.4966,
            "B3": 0.56,
            "B4": 0.6645,
            "B5": 0.7039,
            "B6": 0.7402,
            "B7": 0.7825,
            "B8": 0.8351,
            "B8A": 0.8648,
            "B9": 0.945,
            "B11": 1.6137,
            "B12": 2.2024,
        }


class TestCategoricalBand:
    """Test CategoricalBand."""

    def test_classes(self):
        """Test classes."""
        classes = s2.bands.SCL.class_info.as_dict("value")
        assert classes == {
            "Saturated or defective": 1,
            "Dark Area Pixels": 2,
            "Cloud Shadows": 3,
            "Vegetation": 4,
            "Bare Soils": 5,
            "Water": 6,
            "Clouds Low Probability / Unclassified": 7,
            "Clouds Medium Probability": 8,
            "Clouds High Probability": 9,
            "Cirrus": 10,
            "Snow / Ice": 11,
        }


class TestBitBand:
    """Test BitBand."""

    def test_bitmask(self):
        """Test the bitmask."""
        bitmask = l9.bands.QA_PIXEL.bitmask
        assert bitmask.total == 16
        assert bitmask.to_dict() == {
            "0-0-Fill": {"0": "Image data", "1": "Fill data"},
            "1-1-Dilated Cloud": {"0": "Cloud is not dilated or no cloud", "1": "Cloud dilation"},
            "2-2-Cirrus": {
                "0": "Cirrus Confidence: no confidence level set or Low Confidence",
                "1": "High confidence cirrus",
            },
            "3-3-Cloud": {"0": "Cloud confidence is not high", "1": "High confidence cloud"},
            "4-4-Cloud Shadow": {
                "0": "Cloud Shadow Confidence is not high",
                "1": "High confidence cloud shadow",
            },
            "5-5-Snow": {"0": "Snow/Ice Confidence is not high", "1": "High confidence snow cover"},
            "6-6-Clear": {
                "0": "Cloud or Dilated Cloud bits are set",
                "1": "Cloud and Dilated Cloud bits are not set",
            },
            "7-7-Water": {"0": "Land or cloud", "1": "Water"},
            "8-9-Cloud Confidence": {
                "0": "No confidence level set",
                "1": "Low confidence",
                "2": "Medium confidence",
                "3": "High confidence",
            },
            "10-11-Cloud Shadow Confidence": {
                "0": "No confidence level set",
                "1": "Low confidence",
                "2": "Reserved",
                "3": "High confidence",
            },
            "12-13-Snow / Ice Confidence": {
                "0": "No confidence level set",
                "1": "Low confidence",
                "2": "Reserved",
                "3": "High confidence",
            },
            "14-15-Cirrus Confidence": {
                "0": "No confidence level set",
                "1": "Low confidence",
                "2": "Reserved",
                "3": "High confidence",
            },
        }
