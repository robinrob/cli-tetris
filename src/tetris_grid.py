"""Classes: TetrisGrid."""

from src.grid_square import GridSquare
from src.element import Element
from src.element_type import ElementType
from src.position import Position
from src.movement_type import MovementType
from src.errors import ElementOutOfBoundsException
from src.errors import ElementConflictException


class TetrisGrid:
    """Maintains the state of the Tetris board."""

    WALL_THICKNESS = 1

    def __init__(self, size):
        """Construct a square TetrisGrid with the given size."""
        self._size = size
        self.x_bounds = (0, size - 1)
        self.y_bounds = (0, size - 1)

        # List of rows
        self.grid_squares = []
        # Initialise grid squares
        for column_index in range(0, size):
            column = []
            for row_index in range(0, size):
                column.append(GridSquare())
            self.grid_squares.append(column)

        for row_num in range(*self.y_bounds):
            # Left Wall
            self._get_grid_square(Position(self.x_bounds[0], row_num)).fill_with(Element(ElementType.WALL))
            # Right wall
            self._get_grid_square(Position(self.y_bounds[-1], row_num)).fill_with(Element(ElementType.WALL))

        # Floor
        for col_num in range(*self.y_bounds):
            self._get_grid_square(Position(col_num, self.y_bounds[0])).fill_with(Element(ElementType.WALL))

    def get_lowest_allowed_x_position(self):
        """Return the minimum x coordinate of this grid."""
        return self.x_bounds[0] + TetrisGrid.WALL_THICKNESS

    def get_highest_allowed_x_position(self):
        """Return the maximum x coordinate of this grid."""
        return self.x_bounds[1] - TetrisGrid.WALL_THICKNESS

    def _get_lowest_allowed_y_position(self):
        return self.y_bounds[0] + TetrisGrid.WALL_THICKNESS

    def _get_highest_allowed_y_position(self):
        return self.y_bounds[1] - TetrisGrid.WALL_THICKNESS

    def add_object(self, object):
        """Add the given game object to the grid."""
        for element in object.elements:
            if not self._position_within_bounds(element.position):
                raise ElementOutOfBoundsException(f"Element is out of bounds of grid at {element.position.rounded()}")

            grid_square = self._get_grid_square(element.position)
            if not grid_square.is_empty():
                raise ElementConflictException(
                    f"Element conflicts with existing element in grid at {element.position.rounded()}"
                )

            grid_square.fill_with(element)

    def can_add_object(self, object):
        """Determine whether the given object can be added to the grid."""
        return all([
            self._can_add_element(element)
            for element in object.elements
        ])

    def _can_add_element(self, element):
        return (
            self._position_within_bounds(element.position) and
            self._get_grid_square(element.position).is_empty()
        )

    def remove_object(self, object):
        """Remove the given object from the grid."""
        for element in object.elements:
            grid_square = self._get_grid_square(element.position)
            grid_square.clear()

    def object_has_valid_move(self, object):
        """Determine whether the given object has any possible valid moves at its position."""
        movement_types = [
            MovementType.LEFT,
            MovementType.RIGHT,
            MovementType.ROTATE_CLOCKWISE,
            MovementType.ROTATE_ANTICLOCKWISE
        ]
        for movement_type in movement_types:
            moved_piece = object.moved(movement_type)
            if self.can_add_object(moved_piece):
                return True

        return False

    def _position_within_bounds(self, position):
        return (
            self._position_within_x_bounds(position.x) and
            self._position_within_y_bounds(position.y)
        )

    def _position_within_x_bounds(self, x_pos):
        return x_pos >= self.get_lowest_allowed_x_position() and x_pos <= self.get_highest_allowed_x_position()

    def _position_within_y_bounds(self, y_pos):
        return y_pos >= self._get_lowest_allowed_y_position() and y_pos <= self._get_highest_allowed_y_position()

    def _get_grid_square(self, position):
        return self.grid_squares[int(self._size - 1 - position.rounded().y)][int(position.rounded().x)]