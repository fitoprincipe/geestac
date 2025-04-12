"""The init file of the package."""

__version__ = "0.0.1"
__author__ = "Rodrigo Esteban Principe"
__email__ = "fitoprincipe82@gmail.com"

from .catalog import EECatalog

eecatalog = EECatalog()


def fromId(assetId: str):
    """Load a Catalog or Dataset from an ID."""
    parts = assetId.split("/")
    if len(parts) == 1:
        return eecatalog.children.as_dict()[assetId]()
    else:
        catalog = eecatalog.children.as_dict()[parts[0]]()
        dataset = catalog.children.as_dict()["_".join(parts[1:])]()
        return dataset
