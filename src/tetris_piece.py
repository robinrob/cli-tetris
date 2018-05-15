from src.element import Element
from src.element_type import ElementType
from src.movement_type import MovementType

class TetrisPiece:
    def __init__(self, layout, position):
        self.layout = layout
        if layout is None:
            raise Exception("Layout should not be None")
        self.position = position
        self.elements = [
            Element(ElementType.PIECE, position.cross_product(elem_position))
            for elem_position in layout.positions
        ]

    def moved_down(self):
        return self.moved(MovementType.DOWN)

    def moved(self, movement_type):
        new_position = self.position
        new_layout = self.layout

        if movement_type is MovementType.DOWN:
            new_position = self.position.translated(0, -1)
        if movement_type is MovementType.LEFT:
            new_position = self.position.translated(-1, 0)
        elif movement_type is MovementType.RIGHT:
            new_position = self.position.translated(1, 0)
        elif movement_type is MovementType.ROTATE_CLOCKWISE:
            new_layout = self.layout.rotated(-90)
        elif movement_type is MovementType.ROTATE_ANTICLOCKWISE:
            new_layout = self.layout.rotated(90)

        return TetrisPiece(new_layout, new_position)