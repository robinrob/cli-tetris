class Layout:
    def __init__(self, positions):
        self.positions = positions

    def rotated(self, degrees):
        return Layout([position.rotated(degrees) for position in self.positions])