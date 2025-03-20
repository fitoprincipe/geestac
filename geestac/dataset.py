"""Module to handle GEE Datasets."""

import ee

from .base import STAC


class Dataset(STAC):
    def __init__(self, href: str, parent):
        """Dataset class."""
        super(Dataset, self).__init__(href)
        self.parent = parent

    def _get_interval(self) -> list:
        """Temporal interval."""
        extent = self.data.get("extent", {})
        temporal_resolution = extent.get("temporal", {})
        interval = temporal_resolution.get("interval", [[None, None]])
        return interval

    def _get_summaries(self) -> dict:
        return self.data.get("summaries", {})

    @property
    def start_date(self) -> str | None:
        """Start date of the dataset."""
        try:
            extent = self.data.get("extent", {})
            temporal_resolution = extent.get("temporal", {})
            interval = temporal_resolution.get("interval", [[None, None]])
            return interval[0][0]
            # return self._get_interval()[0][0]
        except KeyError:
            return None

    @property
    def end_date(self) -> str | None:
        """End date of the dataset."""
        try:
            return self._get_interval()[0][1]
        except KeyError:
            return None

    @property
    def extent(self) -> ee.Geometry | None:
        """Spatial Extent."""
        extent = self.data.get("extent", {})
        spatial = extent.get("spatial", {})
        bbox = spatial.get("bbox", None)
        if bbox is not None:
            return ee.Geometry.BBox(bbox[0], bbox[1], bbox[2], bbox[3])
        else:
            return None

    @property
    def eeType(self):
        """Earth Engine Object Type."""
        ty = self.data.get("gee:type")
        types = {
            "table": ee.FeatureCollection,
            "image": ee.Image,
            "image_collection": ee.ImageCollection,
        }
        return types.get(ty)

    @property
    def assetId(self):
        """Earth Engine Asset Id."""
        return self.data.get("id")

    @property
    def eeObject(self):
        """Earth Engine Object."""
        return self.eeType(self.assetId) if self.assetId else None
