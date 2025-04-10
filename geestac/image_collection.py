"""Module to handle ImageCollection Datasets."""

from types import SimpleNamespace

from .image import Image


class ImageCollection(Image):
    def __init__(self, href: str, name: str, parent):
        """ImageCollection Dataset."""
        super(ImageCollection, self).__init__(href=href, name=name, parent=parent)

    @property
    def revisit(self) -> SimpleNamespace:
        """Revisit time.

        Returns:
            a dict as follows: {'interval', 'unit'}
        """
        interval = self.data.get("gee:interval", {})
        if interval.get("type") == "revisit_interval":
            return SimpleNamespace(
                **{"interval": interval.get("interval"), "unit": interval.get("unit")}
            )
        return interval
