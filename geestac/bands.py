"""Module for bands."""

from .custom_types import ListNamespace


class Category:
    """Class that represents a category in a CategoricalBand."""

    def __init__(self, value: int, description: str, color: str | None = None):
        """Initialize a category.

        Args:
            value: value of the category.
            description: description of the category.
            color: color associated to the category (optional).
        """
        self.value = value
        self.description = description
        # TODO: generate a color if not given
        self.color = color


class Bit:
    """Class that represents a single bit."""

    def __init__(self, value: int, description: str):
        """Initialize a Bit.

        Args:
            value: value of the bit.
            description: description of the bit.
        """
        self.value = value
        self.description = description


class BitGroup:
    """Class that represents a bit group."""

    def __init__(self, first: int, count: int, description: str, bits: ListNamespace[Bit]):
        """Initialize a bit group.

        Args:
            first: first bit.
            count: number of bits.
            description: description of the bit information.
            bits: a ListNamespace of Bit objects.
        """
        self.first = first
        self.count = count
        self.description = description
        self.bits = bits

    def to_dict(self) -> dict:
        """Convert a bit group to a dict."""
        start = self.first
        end = self.first + self.count - 1
        bits_key = f"{start}-{end}-{self.description}"
        bits_value = {}
        for bit in self.bits:
            bits_value[str(bit.value)] = bit.description
        return {bits_key: bits_value}


class Bitmask:
    """Class that represents a bit mask in a BitBand."""

    def __init__(self, parts: ListNamespace[BitGroup], total: int):
        """Initialize a bitmask.

        Args:
            parts: a ListNamespace of BitGroup.
            total: total number of bits.
        """
        self.parts = parts
        self.total = total

    def to_dict(self) -> dict:
        """Convert a Bitmask into a dict."""
        final = {}
        for group in self.parts:
            final.update(group.to_dict())
        return final


class Band:
    def __init__(self, name: str, scale: int | float, description: str, range: dict | None = None):
        """General Band class.

        Args:
            name: name of the band.
            scale: spatial resolution.
            description: description of the band.
            range: range of the values.
        """
        self.name = name
        self.scale = scale
        self.description = description
        self._range = range if range is not None else {}

    def __repr__(self):
        """Object representation."""
        return self.name

    @property
    def minimum_value(self) -> int | float | None:
        """If exists in the STAC, return the minimum value."""
        return self._range.get("minimum")

    @property
    def maximum_value(self) -> int | float | None:
        """If exists in the STAC, return the maximum value."""
        return self._range.get("maximum")

    @property
    def estimated_range(self) -> bool | None:
        """If range exists in STAC, return whether the range is estimated or not."""
        return self._range.get("gee:estimated_range")


class OpticalBand(Band):
    def __init__(
        self,
        name: str,
        scale: int | float,
        description: str,
        center_wavelength: int | float | None = None,
        offset: int | float | None = None,
        multiplier: int | float | None = None,
        range: dict | None = None,
    ):
        """Optical Band.

        Args:
            name: name of the band.
            scale: spatial resolution.
            description: description of the band.
            center_wavelength: center wavelength.
            offset: value to "move" the raw value.
            multiplier: value to "multiply" the raw value (GEE calls this value 'scale')
            range: range of the values.
        """
        self.center_wavelength = center_wavelength
        self.offset = offset
        self.multiplier = multiplier
        super(OpticalBand, self).__init__(name, scale, description, range)


class CategoricalBand(Band):
    def __init__(
        self, name: str, scale: int | float, description: str, class_info: ListNamespace[Category]
    ):
        """Categorical Band.

        Args:
            name: name of the band.
            scale: spatial resolution.
            description: description of the band.
            class_info: a ListNamespace with the class value as keys and the
                        class names as values.
        """
        self.class_info = class_info
        super(CategoricalBand, self).__init__(name, scale, description)


class BitBand(Band):
    def __init__(self, name: str, scale: int | float, description: str, bitmask: Bitmask):
        """Bit Band (bits mask).

        Args:
            name: name of the band.
            scale: spatial resolution.
            description: description of the band.
            bitmask: the bit mask.
        """
        self.bitmask = bitmask
        super(BitBand, self).__init__(name, scale, description)
