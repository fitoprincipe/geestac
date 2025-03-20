"""Earth Engine STAC Catalog."""

from .base import STAC


class Catalog(STAC):
    def __init__(self, href: str):
        """Catalog."""
        super(Catalog, self).__init__(href)


class EECatalog(STAC):
    """Earth Engine STAC Catalog.

    This Catalog contains a set of Catalogs accessible via attributes.

    This is always the root for all children.
    """

    URL = "https://earthengine-stac.storage.googleapis.com/catalog/catalog.json"

    def __init__(self):
        """Earth Engine STAC Catalog."""
        super(EECatalog, self).__init__(self.URL)
        self._get_catalogs()

    def _get_catalogs(self):
        """Get all catalogs and set them as instance properties."""
        for link in self.data.get("links", []):
            catalog = Catalog(link["href"])
            if link["rel"] == "child":
                name = link["title"]
                self.__setattr__(name, catalog)
