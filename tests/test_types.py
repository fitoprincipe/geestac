"""Test custom types."""

from geestac.custom_types import ListNamespace


class Tree:
    """Tree class for testing purposes."""

    def __init__(self, genus: str, specie: str):
        """Plant a tree."""
        self.genus = genus
        self.specie = specie


class TestListNamepace:
    """Test ListNamespace."""

    lenga = Tree("Nothofagus", "pumilo")
    laura = Tree("Schinus", "patagonicus")
    ln = ListNamespace(lenga, laura, key="genus")

    def test_as_list_default(self):
        """Test as_list with default params."""
        assert self.ln.as_list() == [self.lenga, self.laura]

    def test_as_list_key(self):
        """Test as_list with key param."""
        assert self.ln.as_list("genus") == ["Nothofagus", "Schinus"]

    def test_as_dict_default(self):
        """Test as_dict with default param."""
        assert self.ln.as_dict() == {"Nothofagus": self.lenga, "Schinus": self.laura}

    def test_as_dict_value(self):
        """Test as_dict with value param."""
        assert self.ln.as_dict("specie") == {"Nothofagus": "pumilo", "Schinus": "patagonicus"}
