"""Module to handle FeatureCollection Datasets."""

from .dataset import Dataset


class FeatureCollection(Dataset):
    def __init__(self, href: str):
        """FeatureCollection Dataset."""
        super(FeatureCollection, self).__init__(href=href)
