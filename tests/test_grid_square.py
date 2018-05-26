"""Unit tests for GridsSquare."""

import unittest

from src.grid_square import GridSquare
from src.element import Element
from src.element_type import ElementType


class GridSquareTestCase(unittest.TestCase):  # noqa: D101
    def test_should_be_empty_on_creation(self):  # noqa: D102
        grid_square = GridSquare()

        self.assertTrue(grid_square.is_empty())

    def test_should_fill_with_element(self):  # noqa: D102
        grid_square = GridSquare()
        element = Element(ElementType.WALL)

        grid_square.fill_with(element)

        self.assertFalse(grid_square.is_empty())

    def test_should_clear(self):  # noqa: D102
        grid_square = GridSquare()
        element = Element(ElementType.WALL)
        grid_square.fill_with(element)

        grid_square.clear()

        self.assertTrue(grid_square.is_empty())