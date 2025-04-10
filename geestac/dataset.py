"""Module to handle GEE Datasets."""

import ee

from .custom_types import ListNamespace
from .stac import STAC


class Property:
    """A class that represents a property."""

    def __init__(self, name: str, type: str, description: str):
        """An object that represents a property.

        Args:
            name: name of the property.
            type: data type of the property.
            description: description of the property.
        """
        self.name = name
        self.type = type
        self.description = description

    def __repr__(self) -> str:
        """Object representation."""
        return f"{self.name} ({self.type})"


class Dataset(STAC):
    def __init__(self, href: str, name: str, parent):
        """Dataset class.

        Args:
            href: the URL.
            name: name of the Dataset.
            parent: the parent Catalog.
        """
        super(Dataset, self).__init__(href, name, parent)

    def __repr__(self) -> str:
        """Object representation."""
        eetype = f" ({self.eeType.name()})" if self.eeType else ""
        status = f" ({self.status})" if self.status else ""
        return f"{self.name}{eetype}{status}"

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
    def spatial_extent(self) -> ee.Geometry | None:
        """Spatial Extent."""
        extent = self.data.get("extent", {})
        spatial = extent.get("spatial", {})
        bbox = spatial.get("bbox", None)
        return bbox

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
    def license(self):
        """License of Use."""
        return self.data.get("license")

    @property
    def assetId(self):
        """Earth Engine Asset Id."""
        return self.data.get("id")

    @property
    def eeObject(self):
        """Earth Engine Object."""
        return self.eeType(self.assetId) if self.assetId else None

    @property
    def status(self):
        """Status of the Dataset."""
        return self.data.get("gee:status")

    @property
    def properties(self) -> ListNamespace:
        """Dataset properties."""
        summ = self.data.get("summaries", {})
        schema = summ.get("gee:schema", [])
        prop = []
        for sch in schema:
            prop.append(Property(sch.get("name"), sch.get("type"), sch.get("description")))
        return ListNamespace(*prop, key="name")

    @property
    def terms_of_use(self):
        """Terms of use."""
        return self.data.get("gee:terms_of_use")
