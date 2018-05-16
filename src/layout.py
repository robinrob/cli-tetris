from src.immutable import Immutable
from src.position import Position


class Layout(Immutable):
    def __init__(self, positions):
        super(Layout, self).__init__(attrs_dict={
            'positions': positions
        })

    def __repr__(self):
        return f"layout: {self.positions}"

    def rotated(self, degrees):
        return Layout([position.rotated(degrees) for position in self.positions])

    def magnified(self, times):
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
        positions = []
        for position in self.positions:
            positions.append(position.dot_product(Position(-1, 1)))

        return Layout(positions)