import random

from src.tetris_grid import TetrisGrid
from src.tetris_piece_factory import TetrisPieceFactory
from src.console_interface import ConsoleInterface
from src.tetris_errors import PieceOutOfBoundsException
from src.movement_type import MovementType
from src.position import Position

class Tetris:
    def __init__(self, user_interface):
        self.user_interface = user_interface

    def play(self):
        game_over = False
        grid = TetrisGrid(20)
        self.user_interface.render_grid(grid)
        piece_factory = TetrisPieceFactory()
        active_piece = self._add_new_piece_to_grid(grid, piece_factory)

        while not game_over:
            moved_active_piece = active_piece.moved_down()

            if self._piece_has_valid_move(active_piece, grid):
                movement_type = self.user_interface.get_player_move()
                moved_active_piece = active_piece.moved(movement_type)
                grid.remove_object(active_piece)
                grid.add_object(moved_active_piece)
                active_piece = moved_active_piece
            else:
                try:
                    active_piece = self._add_new_piece_to_grid(grid, piece_factory)

                except PieceOutOfBoundsException:
                    game_over = True

        print("GAME OVER!")

    def _piece_has_valid_move(self, piece, grid):
        movement_types = [
            MovementType.LEFT,
            MovementType.RIGHT,
            MovementType.ROTATE_CLOCKWISE,
            MovementType.ROTATE_CLOCKWISE
        ]
        for movement_type in movement_types:
            moved_piece = piece.moved(movement_type)
            if grid.can_add_object(moved_piece):
                return True
            
        return False

    def _add_new_piece_to_grid(self, grid, piece_factory):
        xPos = random.randint(
            grid.get_lowest_allowed_x_position(),
            grid.get_highest_allowed_x_position()
        )
        position = Position(10, 10)
        piece = piece_factory.get_random_piece_at_position(position)
        print('position: %s' % position)

        if grid.can_add_object(piece):
            grid.add_object(piece)
        else:
            raise PieceOutOfBoundsException

        return piece