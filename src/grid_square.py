"""Classes: GridSquare."""


class GridSquare:
    """
    GridSquare represents a single square of the Tetris board and can be filled and cleared.

    GridSquare is effectively a 'unit' of game state.

    When GridSquare is occupied, it maintains a reference to the Element occupying it.
    """

    def __init__(self):
        """Construct an empty GridSquare."""
        self.occupied_by = None

    def __repr__(self):
        """Generate text representation of this GridSquare."""
        if self.is_empty():
            return " "
        else:
            return "*"

    def is_empty(self, ignore_elements=[]):
        """Indicate whether the GridSquare is empty."""
        return self.occupied_by is None or self.occupied_by in ignore_elements

    def fill_with(self, element):
        """Fill this GridSquare with the given Element."""
        self.occupied_by = element

    def clear(self):
        """Clear this GridSquare."""
        self.occupied_by = None
