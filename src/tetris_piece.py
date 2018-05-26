"""Classes: Tetris Piece."""

from src.element import Element
from src.element_type import ElementType
from src.movement_type import MovementType
from src.errors import InvalidMoveException
from src.immutable import Immutable
from settings import MOVE_UNITS


class TetrisPiece(Immutable):
    """Represents a Tetris piece."""

    def __init__(self, layout, position):
        """Construct a TetrisPiece using the given Layout located at the given Position."""
        super(TetrisPiece, self).__init__(attrs_dict={
            'layout': layout,
            'position': position,
            'elements': [
                Element(ElementType.PIECE, position.add(elem_position))
                for elem_position in layout.positions
            ]
        })

    def moved_down(self):
        """Return a new version of this TetrisPiece translated downwards by one unit."""
        return self.moved(MovementType.DOWN)

    def moved(self, movement_type):
        """Return a new version of this TetrisPiece moved according to the given MovementType."""
        new_position = self.position
        new_layout = self.layout

        if movement_type == MovementType.NONE:
            pass
        elif movement_type == MovementType.DOWN:
            new_position = self.position.translated(0, -MOVE_UNITS)
        elif movement_type == MovementType.LEFT:
            new_position = self.position.translated(-MOVE_UNITS, 0)
        elif movement_type == MovementType.RIGHT:
            new_position = self.position.translated(MOVE_UNITS, 0)
        elif movement_type == MovementType.ROTATE_CLOCKWISE:
            new_layout = self.layout.rotated(-90)
        elif movement_type == MovementType.ROTATE_ANTICLOCKWISE:
            new_layout = self.layout.rotated(90)
        else:
            raise InvalidMoveException(f"Invalid movement type: {movement_type}")

        return TetrisPiece(new_layout, new_position)