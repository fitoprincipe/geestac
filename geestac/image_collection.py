"""Module to handle ImageCollection Datasets."""

from .dataset import Dataset


class ImageCollection(Dataset):
    def __init__(self, href: str):
        """ImageCollection Dataset."""
        super(ImageCollection, self).__init__(href=href)
