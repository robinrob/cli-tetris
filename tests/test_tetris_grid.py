"""Unit tests for TetrisGrid."""

import unittest

from src.tetris_grid import TetrisGrid
from src.tetris_piece import TetrisPiece
from src.layout import Layout
from src.position import Position
from src.errors import ElementOutOfBoundsException
from src.errors import ElementConflictException


class TetrisGridTestCase(unittest.TestCase):  # noqa: D101
    def test_should_return_lowest_allowed_x_position(self):  # noqa: D102
        grid = TetrisGrid(10)

        lowest_x = grid.get_lowest_allowed_x_position()

        self.assertEquals(1, lowest_x)

    def test_should_return_highest_allowed_x_position(self):  # noqa: D102
        grid = TetrisGrid(10)

        highest_x = grid.get_highest_allowed_x_position()

        self.assertEquals(8, highest_x)

    def test_grid_should_allow_adding_object_when_object_within_bounds(self):  # noqa: D102
        grid = TetrisGrid(10)
        # Single element at (5, 5) should fit within wall bounds
        layout = Layout([Position(0, 0)])
        object = TetrisPiece(layout, Position(5, 5))

        can_add_object = grid.can_add_object(object)

        self.assertTrue(can_add_object)

    def test_should_add_object_when_object_within_bounds(self):  # noqa: D102
        grid = TetrisGrid(10)
        # Single element at (5, 5) should fit within wall bounds
        layout = Layout([Position(0, 0)])
        object = TetrisPiece(layout, Position(5, 5))

        grid.add_object(object)

    def test_should_should_raise_out_of_bounds_exception_when_attempting_to_add_object_out_of_bounds(self):  # noqa: D102
        grid = TetrisGrid(10)
        # Single element at (0, 0) overlaps with floor
        layout = Layout([Position(-1, -1)])
        object = TetrisPiece(layout, Position(0, 0))

        with self.assertRaises(ElementOutOfBoundsException):
            grid.add_object(object)

    def test_should_should_raise_out_of_bounds_exception_when_attempting_to_add_object_overlapping_wall(self):  # noqa: D102
        grid = TetrisGrid(10)
        # Single element at (0, 0) overlaps with floor
        layout = Layout([Position(0, 0)])
        object = TetrisPiece(layout, Position(0, 0))

        with self.assertRaises(ElementOutOfBoundsException):
            grid.add_object(object)

    def test_should_should_raise_conflict_exception_when_attempting_to_add_overlapping_object(self):  # noqa: D102
        grid = TetrisGrid(10)
        layout = Layout([Position(0, 0)])
        object = TetrisPiece(layout, Position(5, 5))

        grid.add_object(object)
        with self.assertRaises(ElementConflictException):
            grid.add_object(object)

    def test_should_remove_object(self):  # noqa: D102
        grid = TetrisGrid(10)
        # Single element at (5, 5) should fit within wall bounds
        layout = Layout([Position(0, 0)])
        object = TetrisPiece(layout, Position(5, 5))
        grid.add_object(object)

        grid.remove_object(object)

        grid.add_object(object)

    def test_object_should_have_valid_move(self):  # noqa: D102
        grid = TetrisGrid(10)
        layout = Layout([
            Position(0, 0),
            Position(1, 0),
            Position(0, 1),
            Position(1, 1)
        ])
        object = TetrisPiece(layout, Position(4, 8))

        has_valid_move = grid.object_has_valid_move(object)

        self.assertTrue(has_valid_move)

    def test_object_should_have_valid_move_when_1_space_above_floor(self):  # noqa: D102
        grid = TetrisGrid(10)
        layout = Layout([
            Position(0, 0),
            Position(1, 0),
            Position(0, 1),
            Position(1, 1)
        ])
        object = TetrisPiece(layout, Position(5, 1))

        has_valid_move = grid.object_has_valid_move(object)

        self.assertTrue(has_valid_move)

    def test_object_should_not_have_valid_move_when_already_on_floor(self):  # noqa: D102
        grid = TetrisGrid(10)
        layout = Layout([
            Position(0, 0),
            Position(1, 0),
            Position(0, 1),
            Position(1, 1)
        ])
        object = TetrisPiece(layout, Position(5, 0))

        has_valid_move = grid.object_has_valid_move(object)

        self.assertFalse(has_valid_move)