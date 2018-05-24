import unittest

from src.tetris_piece import TetrisPiece
from src.layout import Layout
from src.position import Position
from src.movement_type import MovementType
from settings import MOVE_UNITS


class TetrisPieceTestCase(unittest.TestCase):
    def test_should_initialise_elements_in_positions_according_to_layout(self):
        layout = Layout([
            # Absolute position = (5, 6)
            Position(0, 1),
            # Absolute position = (6, 5)
            Position(1, 0),
            # Absolute position = (6, 6)
            Position(1, 1),
        ])
        position = Position(5, 5)
        piece = TetrisPiece(layout, position)

        self.assertEquals(3, len(piece.elements))
        self.assertEquals(Position(5, 6), piece.elements[0].position)
        self.assertEquals(Position(6, 5), piece.elements[1].position)
        self.assertEquals(Position(6, 6), piece.elements[2].position)

    def test_should_move_down(self):
        layout = Layout([
            Position(0, 1),
            Position(1, 0),
            Position(1, 1),
        ])
        position = Position(5, 5)
        piece = TetrisPiece(layout, position)

        new_piece = piece.moved_down()

        self.assertEquals(Position(5, 5 - MOVE_UNITS), new_piece.position)
        self.assertEquals(Position(6, 6 - MOVE_UNITS), new_piece.elements[2].position)

    def test_should_move_left(self):
        layout = Layout([
            Position(0, 1),
            Position(1, 0),
            Position(1, 1),
        ])
        position = Position(5, 5)
        piece = TetrisPiece(layout, position)

        new_piece = piece.moved(MovementType.LEFT)

        self.assertEquals(Position(5 - MOVE_UNITS, 5), new_piece.position)
        self.assertEquals(Position(6 - MOVE_UNITS, 6), new_piece.elements[2].position)

    def test_should_move_right(self):
        layout = Layout([
            Position(0, 1),
            Position(1, 0),
            Position(1, 1),
        ])
        position = Position(5, 5)
        piece = TetrisPiece(layout, position)

        new_piece = piece.moved(MovementType.RIGHT)

        self.assertEquals(Position(5 + MOVE_UNITS, 5), new_piece.position)
        self.assertEquals(Position(6 + MOVE_UNITS, 6), new_piece.elements[2].position)

    def test_should_rotate_clockwise(self):
        layout = Layout([
            Position(0, 1),
            Position(1, 0),
            Position(1, 1),
        ])
        position = Position(5, 5)
        piece = TetrisPiece(layout, position)

        new_piece = piece.moved(MovementType.ROTATE_CLOCKWISE)

        self.assertEquals(Position(5, 5), new_piece.position)
        self.assertEquals(Position(6, 5), new_piece.elements[0].position)
        self.assertEquals(Position(5, 4), new_piece.elements[1].position)
        self.assertEquals(Position(6, 4), new_piece.elements[2].position)

    def test_should_rotate_anticlockwise(self):
        layout = Layout([
            Position(0, 1),
            Position(1, 0),
            Position(1, 1),
        ])
        position = Position(5, 5)
        piece = TetrisPiece(layout, position)

        new_piece = piece.moved(MovementType.ROTATE_ANTICLOCKWISE)

        self.assertEquals(Position(5, 5), new_piece.position)
        self.assertEquals(Position(4, 5), new_piece.elements[0].position)
        self.assertEquals(Position(5, 6), new_piece.elements[1].position)
        self.assertEquals(Position(4, 6), new_piece.elements[2].position)
