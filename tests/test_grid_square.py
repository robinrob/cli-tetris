import unittest

from grid_square import GridSquare
from element import Element
from element_type import ElementType


class GridSquareTestCase(unittest.TestCase):
    def test_should_be_empty_on_creation(self):
        grid_square = GridSquare()

        self.assertTrue(grid_square.is_empty())


    def test_should_fill_with_element(self):
        grid_square = GridSquare()
        element = Element(ElementType.WALL)

        grid_square.fill_with(element)

        self.assertFalse(grid_square.is_empty())


    def test_should_clear(self):
        grid_square = GridSquare()
        element = Element(ElementType.WALL)
        grid_square.fill_with(element)

        grid_square.clear()

        self.assertTrue(grid_square.is_empty())