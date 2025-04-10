"""Test helpers."""

from geestac import helpers


class TestHelpers:
    """Test helpers."""

    def test_format_attribute(self):
        """Test format_attribute function."""
        attr = "hello world - 1.1"
        expected = "hello_world___1_1"
        assert helpers.format_attribute(attr) == expected
