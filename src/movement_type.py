from enum import Enum

class MovementType(Enum):
    NONE = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    ROTATE_CLOCKWISE = 4
    ROTATE_ANTICLOCKWISE = 5

    def __eq__(self, other):
        return self.value == other.value