"""Helpers for this package."""


def format_attribute(attribute: str) -> str:
    """Convert characters from any attribute to match the format of class/object attributes.

    Args:
        attribute: an attribute.
    """
    to_replace = "- ."
    for char in to_replace:
        attribute = attribute.replace(char, "_")
    return attribute
