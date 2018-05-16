from src.immutable import Immutable
from src.position import Position


class Layout(Immutable):
    def __init__(self, positions):
        super(Layout, self).__init__(attrs_dict={
            'positions': positions
        })

    def rotated(self, degrees):
        return Layout([position.rotated(degrees) for position in self.positions])

    def magnified(self, times):
        positions = []
        for position in self.positions:
            positions.append(position)
            for i in range(times):
                positions.append(position.add(Position(i, 0)))
                positions.append(position.add(Position(0, i)))
                positions.append(position.add(Position(i, i)))
                
        return Layout(set(positions))

    def flipped_horizontally(self, layout):
        positions = []
        for position in self.positions:
            positions.append(position.dot_product(Position(-1, 1)))

        return Layout(positions)