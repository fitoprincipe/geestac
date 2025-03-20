"""Module to handle Image Datasets."""

from .dataset import Dataset


class Image(Dataset):
    def __init__(self, href: str):
        """Image Dataset."""
        super(Image, self).__init__(href=href)
