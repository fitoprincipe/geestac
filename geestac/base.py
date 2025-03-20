"""STAC Base class."""

import requests


class STAC:
    """Base STAC class."""

    def __init__(self, href: str):
        """Base STAC class.

        Args:
            href: URL of the catalog / dataset
        """
        self.href = href
        self._data = {}

    @property
    def data(self):
        """Dataset raw data as dict."""
        if len(self._data) == 0:
            self._data = requests.get(self.href).json()
        return self._data

    @property
    def description(self):
        """Description of the Catalog."""
        return self.data.get("description", "")

    @property
    def version(self):
        """STAC Version."""
        return self.data.get("stac_version")

    @property
    def name(self):
        """STAC name (ID)."""
        return self.data.get("id")
