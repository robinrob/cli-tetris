from src.immutable import Immutable


class Layout(Immutable):
    def __init__(self, positions):
        super(Layout, self).__init__(attrs_dict={
            'positions': positions
        })

    def rotated(self, degrees):
        return Layout([position.rotated(degrees) for position in self.positions])
