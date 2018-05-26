"""Classes: Tetris."""

import random

from src.tetris_grid import TetrisGrid
from src.tetris_piece_factory import Layouts
from src.tetris_piece_factory import TetrisPieceFactory
from src.errors import GameOverException
from src.position import Position
from settings import GRID_SIZE
from src.immutable import Immutable
from src.movement_type import MovementType


class Tetris(Immutable):
    """
    Tetris contains the game logic for CLI Tetris.

    The game logic is totally independent of its user interface.

    Tetris makes calls to its user interface to obtain user input and render the tetris board.
    """

    def __init__(self, user_interface):
        """Construct a new Tetris game with the given user interface."""
        super(Tetris, self).__init__(attrs_dict={
            'user_interface': user_interface
        })

    def play(self):
        """Play a game of Tetris."""
        game_over = False
        grid = TetrisGrid(GRID_SIZE)
        piece_factory = TetrisPieceFactory()
        self.user_interface.render_hello_message()

        try:
            active_piece = self._add_new_piece_to_grid(grid, piece_factory)
            self.user_interface.render_grid(grid)

            while not game_over:
                grid.remove_object(active_piece)

                # Check if piece can be be moved by player in-place
                # Get player move and add piece in new position if valid move
                moved = False
                if grid.object_has_valid_move(active_piece):
                    movement_type = self.user_interface.get_player_move()
                    if movement_type is not MovementType.NONE:
                        moved_piece = active_piece.moved(movement_type)

                        if grid.can_add_object(moved_piece):
                            active_piece = moved_piece
                            moved = True

                # Check if piece can be moved down
                # Check if piece can still be added after moving downwards after move
                # TODO: need to check fractions of downward move when MOVE_UNITS > 1
                moved_piece = active_piece.moved_down()
                if grid.can_add_object(moved_piece):
                    active_piece = moved_piece
                    moved = True

                grid.add_object(active_piece)

                if not moved:
                    active_piece = self._add_new_piece_to_grid(grid, piece_factory)

                self.user_interface.render_grid(grid)

        except GameOverException as e:
            self.user_interface.render_game_over_message(grid)

    def _add_new_piece_to_grid(self, grid, piece_factory):
        xPos = random.randint(
            grid.get_lowest_allowed_x_position() + Layouts.MAX_DIMENSION,
            grid.get_highest_allowed_x_position() - Layouts.MAX_DIMENSION
        )
        position = Position(xPos, grid.y_bounds[1] - Layouts.MAX_DIMENSION)
        piece = piece_factory.get_random_piece_at_position(position)

        if grid.can_add_object(piece):
            grid.add_object(piece)
        else:
            raise GameOverException("New piece cannot be added to board!")

        return piece