class Element:
    def __init__(self, type, position=None):
        self.type = type
        self.position = position if position is None else position.rounded()
