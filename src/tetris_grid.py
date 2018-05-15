import random

from src.grid_square import GridSquare
from src.element import Element
from src.element_type import ElementType

class TetrisGrid:
    def __init__(self, size):
        self._size = size
        self.x_bounds = (0, size - 1)
        self.y_bounds = (0, size - 1)

        # List of rows
        self.grid_squares = []
        for column_index in range(0, size):
            column = []
            for row_index in range(0, size):
                column.append(GridSquare())

            self.grid_squares.append(column)

        from src.position import Position
        # self._get_grid_square(Position(10, 1)).fill_with(Element(ElementType.WALL))

        for row_num in range(*self.y_bounds):
            # Left Wall
            self._get_grid_square(Position(self.x_bounds[0], row_num)).fill_with(Element(ElementType.WALL))
            # Right wall
            self._get_grid_square(Position(self.y_bounds[-1], row_num)).fill_with(Element(ElementType.WALL))
        
        # Floor 
        for col_num in range(*self.y_bounds):
            self._get_grid_square(Position(col_num, self.y_bounds[0])).fill_with(Element(ElementType.WALL))

    def get_lowest_allowed_x_position(self):
        return self.x_bounds[0]+1

    def get_highest_allowed_x_position(self):
        return self.x_bounds[1]-1

    def add_object(self, object):
        for element in object.elements:
            pos = element.position
            self.grid_squares[pos.y][pos.x].clear()


    def can_add_object(self, object):
        return all([
            self._can_add_element(element)     
            for element in object.elements
        ])

    def _can_add_element(self, element):
        return self._position_within_bounds(element.position) and self._get_grid_square(element.position).is_empty()

    def _position_within_bounds(self, position):
        return position.x >= self.x_bounds[0] and position.x <= self.x_bounds[1] and position.y >= self.y_bounds[0] and position.y <= self.y_bounds[1]

    def add_object(self, object):
        for element in object.elements:
            self._get_grid_square(element.position).fill_with(element)

    def _get_grid_square(self, position):
        return self.grid_squares[int(self._size - 1 - position.y)][int(position.x)]