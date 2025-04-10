"""Module to handle FeatureCollection Datasets."""

from .dataset import Dataset


class FeatureCollection(Dataset):
    def __init__(self, href: str, name: str, parent):
        """Feature Collection."""
        super(FeatureCollection, self).__init__(href, name, parent)
