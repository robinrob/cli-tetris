import random

from src.tetris_grid import TetrisGrid
from src.tetris_piece_factory import TetrisPieceFactory
from src.console_interface import ConsoleInterface
from src.tetris_errors import GameOverException
from src.position import Position

class Tetris:
    def __init__(self, user_interface):
        self.user_interface = user_interface

    def play(self):
        game_over = False
        grid = TetrisGrid(20)
        piece_factory = TetrisPieceFactory()

        try:
            active_piece = self._add_new_piece_to_grid(grid, piece_factory)
            self.user_interface.render_grid(grid)

            while not game_over:
                moved_active_piece = active_piece.moved_down()

                if self._piece_has_valid_move(active_piece, grid):
                    movement_type = self.user_interface.get_player_move()
                    moved_active_piece = active_piece.moved(movement_type)
                    grid.remove_object(active_piece)
                    grid.add_object(moved_active_piece)
                    active_piece = moved_active_piece
                else:
                    active_piece = self._add_new_piece_to_grid(grid, piece_factory)

                self.user_interface.render_grid(grid)

        except GameOverException as e:
            print('e.msg: %s' % e.message)

            pass
            

    def _add_new_piece_to_grid(self, grid, piece_factory):
        xPos = random.randint(
            grid.get_lowest_allowed_x_position()+3,
            grid.get_highest_allowed_x_position()-3
        )
        position = Position(xPos, grid.y_bounds[1]-4)
        piece = piece_factory.get_random_piece_at_position(position)

        if grid.can_add_object(piece):
            grid.add_object(piece)
        else:
            raise GameOverException("New piece cannot be added to board!")

        return piece