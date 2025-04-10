"""Module to handle Image Datasets."""

from .bands import Band, Bit, BitBand, BitGroup, Bitmask, CategoricalBand, Category, OpticalBand
from .custom_types import ListNamespace
from .dataset import Dataset


class Image(Dataset):
    def __init__(self, href: str, name: str, parent):
        """Image Dataset."""
        super(Image, self).__init__(href=href, name=name, parent=parent)
        self._bands = ListNamespace(key="name")

    @property
    def bands(self) -> ListNamespace:
        """Image bands."""
        if len(self._bands) == 0:
            bands = []
            summ = self._get_summaries()
            eobands = summ.get("eo:bands", [])
            general_scale = summ.get("gsd")
            if isinstance(general_scale, (list, tuple)):
                # TODO: check/investigate why it's a list and what happens if it has more than 1 item
                general_scale = general_scale[0]
            for band in eobands:
                name = band.get("name")
                scale = band.get("gsd", general_scale)
                desc = band.get("description")
                range = self._get_summaries().get(name, {})
                if "gee:wavelength" in band or "center_wavelength" in band:
                    # OpticalBand
                    center_wl = band.get("center_wavelength")
                    offset = band.get("offset", 0)
                    multiplier = band.get("scale", 0)
                    b = OpticalBand(name, scale, desc, center_wl, offset, multiplier, range)
                elif "gee:classes" in band:
                    # CategoricalBand
                    classes = band.get("gee:classes")
                    cat_list = []
                    for cls in classes:
                        cat = Category(cls["value"], cls["description"], cls.get("color"))
                        cat_list.append(cat)
                    class_info = ListNamespace(*cat_list, key="description")
                    b = CategoricalBand(name, scale, desc, class_info)
                elif "gee:bitmask" in band:
                    # BitBand
                    bitmask_raw = band.get("gee:bitmask")
                    parts = bitmask_raw["bitmask_parts"]
                    bit_groups = []
                    for part in parts:
                        bits = []
                        values = part.get("values")
                        if not values:
                            continue
                        for value in values:
                            bit = Bit(value["value"], value["description"])
                            bits.append(bit)
                        bitsns = ListNamespace(*bits, key="description")
                        group = BitGroup(
                            part["first_bit"], part["bit_count"], part["description"], bitsns
                        )
                        bit_groups.append(group)
                    partsns = ListNamespace(*bit_groups, key="description")
                    bitmask = Bitmask(partsns, bitmask_raw["total_bit_count"])
                    b = BitBand(name, scale, desc, bitmask)
                else:
                    b = Band(name, scale, desc, range)
                bands.append(b)
            self._bands = ListNamespace(*bands, key="name")
        return self._bands
