"""Earth Engine STAC Catalog."""

import re
from typing import Union

import requests

from .custom_types import ListNamespace
from .dataset import Dataset
from .feature_collection import FeatureCollection
from .image import Image
from .image_collection import ImageCollection
from .stac import STAC


class LazyDataset(STAC):
    def __init__(self, href: str, name: str, parent):
        """Catalog."""
        super(LazyDataset, self).__init__(href, name, parent)
        self.data = {}

    def __call__(self):
        """Fetch data and return the corresponding object."""
        super(LazyDataset, self).__call__()
        eetype = self.data.get("gee:type")
        if eetype == "image":
            # fetch data here
            ds = Image(self.href, self.name, self.parent)()
        elif eetype == "image_collection":
            ds = ImageCollection(self.href, self.name, self.parent)()
        elif eetype == "table":
            ds = FeatureCollection(self.href, self.name, self.parent)()
        else:
            ds = Dataset(self.href, self.name, self.parent)()
        return ds


class Catalog(STAC):
    def __init__(self, href: str, name: str, parent):
        """Catalog."""
        super(Catalog, self).__init__(href, name, parent)
        self.data = {}
        self.children: ListNamespace[Union[Dataset, LazyDataset]] = ListNamespace(key="name")

    def __call__(self):
        """Fetch data."""
        if self.is_lazy():
            self.data = requests.get(self.href).json()
            self._get_datasets()
            self._lazy = False
        return self

    def _get_datasets(self):
        """Get all catalogs and set them as instance properties."""
        for link in self.data.get("links", []):
            if link["rel"] == "child":
                name = link["title"].replace("-", "_")
                if re.match(f"^{self.name}", name):
                    name = name.replace(f"{self.name}_", "")
                catalog = LazyDataset(link["href"], name, self)
                # setattr(self.children, name, catalog)
                self.children._append(catalog)
                self.__setattr__(name, catalog)


class EECatalog(STAC):
    """Earth Engine STAC Catalog.

    This Catalog contains a set of Catalogs accessible via attributes.

    This is always the root for all children.
    """

    base_url = "https://earthengine-stac.storage.googleapis.com/catalog/catalog.json"

    def __init__(self):
        """Earth Engine STAC Catalog."""
        super(EECatalog, self).__init__(self.base_url, "EECatalog")
        # self.children = DictNamespace()
        self.children = ListNamespace(key="name")
        self.data = requests.get(self.base_url).json()
        self._get_catalogs()

    def _get_catalogs(self):
        """Get all catalogs and set them as instance properties."""
        for link in self.data.get("links", []):
            if link["rel"] == "child":
                name = link["title"].replace("-", "_")
                catalog = Catalog(link["href"], name, self)
                if re.match(f"^{self.name}", name):
                    name = name.replace(f"{self.name}_", "")
                # setattr(self.children, name, catalog)
                # self.children[name] = catalog
                self.children._append(catalog)
                self.__setattr__(name, catalog)
