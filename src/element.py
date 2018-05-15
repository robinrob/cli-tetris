class Element:
    def __init__(self, type, position=None):
        self.type = type
        self.position = position if position is None else position.rounded()

    def translate(x, y):
        self.position = self.position.translate(x, y)
    
    def rotate(degrees, pivot_pos):
        self.position = self.position.rotated(degrees, pivot_pos)