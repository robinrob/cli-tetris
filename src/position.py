"""Classes: Position."""

import math
import hashlib

from src.immutable import Immutable


class Position(Immutable):
    """Holds an x-y coordinate pair. Can be used to represent a point or a vector for example."""

    def __init__(self, x, y):
        """Construct a Position from x and y values."""
        super(Position, self).__init__(attrs_dict={
            'x': x,
            'y': y
        })

    def __eq__(self, other):
        """Determine equality with another Position."""
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        """Generate a hash of this Position."""
        return int(hashlib.md5(self.__repr__().encode()).hexdigest(), 16)

    def __repr__(self):
        """Generate text representation of this Position."""
        return f"({self.x}, {self.y})"

    def translated(self, x, y):
        """Return a new version of this Position translated by the given x and y amounts."""
        return Position(self.x + x, self.y + y)

    def relative_to(self, other_point):
        """Return a new version of this Position relative to the given Position."""
        return Position(self.x - other_point.x, self.y - other_point.y)

    def rotated(self, degrees):
        """Return a new version of this Position rotated by the given amount about (0, 0)."""
        rad = math.pi / 180 * degrees

        return Position(
            self.x * math.cos(rad) - self.y * math.sin(rad),
            self.x * math.sin(rad) + self.y * math.cos(rad)
        )

    def rotated_around_pivot(self, pivot_pos, degrees):
        """Return a new version of this Position rotated by the given amount about the given pivot point."""
        rel_pos = self.relative_to(pivot_pos)
        new_rel_pos = rel_pos.rotated(degrees)

        return Position(
            new_rel_pos.x + pivot_pos.x,
            new_rel_pos.y + pivot_pos.y
        )

    def rounded(self, places=0):
        """Return a new version of this Position with the coordinates rounded to the given number of places."""
        return Position(round(self.x, places), round(self.y, places))

    def add(self, other_point):
        """Return the vector sum of this Position with another Position."""
        return Position(self.x + other_point.x, self.y + other_point.y)

    def dot_product(self, other_point):
        """Return the dot product of this Position with another Position."""
        return Position(self.x * other_point.x, self.y * other_point.y)