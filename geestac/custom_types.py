"""Custom types."""

import json
import logging
from typing import Any, Generic, TypeVar

from .helpers import format_attribute

logger = logging.getLogger("geestac")

# Create a TypeVar for generic typing
T = TypeVar("T")


class ListNamespace(Generic[T]):
    """A Namespace to store objects with a unique attribute (key)."""

    def __init__(self, *args: T, key: str):
        """A Namespace to store objects with a unique attribute (key).

        If the value of the key is not suitable for an attribute, it'll be
        converted with format_attribute function. The values of the keys must
        be unique, else the first occurrence will be kept.

        Args:
            args: a list of objects.
            key: the attribute of the object to get the key from.
        """
        self._key = key
        self._args = ()
        for obj in args:
            self.__setattr__(getattr(obj, key), obj)

    def keys(self) -> list:
        """Key values as list."""
        return [getattr(obj, self._key) for obj in self._args]

    def __setattr__(self, key: str, value: Any):
        """Set attribute to this object."""
        if key in ["_key", "_args"]:
            super().__setattr__(key, value)
            return self
        key = format_attribute(key)
        try:
            getattr(self, key)
        except AttributeError:
            args = list(self._args)
            args.append(value)
            self._args = tuple(args)
            super().__setattr__(key, value)
        else:
            raise AttributeError(f"object with attribute {self._key} = {key} already exists.")
        return self

    def as_list(self, key: str | None = None) -> list:
        """ListNamespace as list.

        Args:
            key: attribute of the object to put in the list. If None it will put the objects in the list.
        """
        if key is None:
            return list(self._args)
        else:
            args = []
            for arg in self._args:
                try:
                    attr = getattr(arg, key)
                except AttributeError:
                    continue
                else:
                    args.append(attr)
            return args

    def as_dict(self, value: str | None = None) -> dict:
        """ListNamespace as a dict.

        Args:
            value: attribute of the object to use as value.
        """
        keys = self.as_list(self._key)
        values = self.as_list(value)
        return dict(zip(keys, values))

    def __repr__(self):
        """Object representation."""
        return json.dumps([item for item in self.as_list(self._key)])

    def __getitem__(self, index: int | str):
        """Get item from ListNamepace.

        Args:
            index: index of the element in the ListNamespace.
        """
        if isinstance(index, int):
            return self._args[index]
        else:
            return self.as_dict()[str]

    def __len__(self):
        """Length of the ListNamespace."""
        return len(self._args)

    def _append(self, obj: Any):
        """Append an object to the list."""
        key = getattr(obj, self._key)
        return self.__setattr__(key, obj)

    def is_empty(self) -> bool:
        """Is this object empty?."""
        return len(self.as_list()) == 0

    def __iter__(self):
        """Iterator."""
        return iter(self._args)
