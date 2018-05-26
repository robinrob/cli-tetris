"""Classes: Layout."""

from src.immutable import Immutable
from src.position import Position


class Layout(Immutable):
    """Represents a layout for a game object."""

    def __init__(self, positions):
        """
        Construct a Layout from a list of Position instances.

        The co-ordinates of each Position should be relative to the origin of the Layout.

        Example:
        Layout([
            Position(0, 0),
            Position(0, 1),
            Position(1, 0)
        ])
        Results in the following Layout:
        *
        * *
        """
        super(Layout, self).__init__(attrs_dict={
            'positions': positions
        })

    def __repr__(self):
        """Return text representation."""
        return f"layout: {self.positions}"

    def rotated(self, degrees):
        """Return a new verson of this Layout rotated by the given degrees about its origin."""
        return Layout([position.rotated(degrees) for position in self.positions])

    def magnified(self, times):
        """Return a new verson of this Layout magnified by the given factor."""
        if times > 1:
            positions = []
            for position in self.positions:
                positions.append(position)
                positions.append(position.add(Position(1, 0)))
                positions.append(position.add(Position(0, 1)))
                positions.append(position.add(Position(1, 1)))

            return Layout(set(positions)).magnified(times - 1)
        else:
            return Layout(set(self.positions))

    def flipped_horizontally(self):
        """Return a new verson of this Layout flipped horizontally about its origin."""
        positions = []
        for position in self.positions:
            positions.append(position.dot_product(Position(-1, 1)))

        return Layout(positions)