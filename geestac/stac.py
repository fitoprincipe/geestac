"""STAC Base class."""

import requests


class STAC:
    """Base STAC class."""

    def __init__(self, href: str, name: str, parent=None):
        """Base STAC class.

        Fetch the STAC data at init.

        Args:
            href: URL of the catalog / dataset.
            name: name of the catalog / dataset.
            parent: parent STAC class.
        """
        self.href = href
        self.name = name
        self.data: dict = {}
        self.parent = parent
        self._lazy = True

    def is_lazy(self) -> bool:
        """Lazy means it has not fetched the real data yet."""
        return self._lazy

    def __repr__(self):
        """Object representation."""
        return f"{self.name}{' (lazy)' if self.is_lazy() else ''}"

    @property
    def description(self):
        """Description of the Catalog."""
        return self.data.get("description")

    @property
    def version(self):
        """STAC Version."""
        return self.data.get("stac_version")

    def __call__(self):
        """Fetch the data."""
        if self.is_lazy():
            self.data = requests.get(self.href).json()
            self._lazy = False
        return self

    def __eq__(self, other):
        """Compare with another object."""
        if not isinstance(other, STAC):
            return False
        data = self.data == other.data
        name = self.name == other.name
        return data and name
