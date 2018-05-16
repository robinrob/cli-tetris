import random

from src.tetris_grid import TetrisGrid
from src.tetris_piece_factory import TetrisPieceFactory
from src.errors import GameOverException
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
                if grid.object_has_valid_move(active_piece):
                    grid.remove_object(active_piece)
                    movement_type = self.user_interface.get_player_move()
                    moved_piece = active_piece.moved(movement_type)

                    # Check if piece can be added after player move
                    if grid.can_add_object(moved_piece):
                        active_piece = moved_piece

                    # Check if piece can still be added after moving downwards after move
                    moved_piece = active_piece.moved_down()
                    if grid.can_add_object(moved_piece):
                        active_piece = moved_piece

                    grid.add_object(active_piece)
                    active_piece = moved_piece

                else:
                    active_piece = self._add_new_piece_to_grid(grid, piece_factory)

                self.user_interface.render_grid(grid)

        except GameOverException as e:
            pass

    def _add_new_piece_to_grid(self, grid, piece_factory):
        xPos = random.randint(
            grid.get_lowest_allowed_x_position() + TetrisPieceFactory.MAX_DIMENSION,
            grid.get_highest_allowed_x_position() - TetrisPieceFactory.MAX_DIMENSION
        )
        position = Position(xPos, grid.y_bounds[1] - TetrisPieceFactory.MAX_DIMENSION)
        piece = piece_factory.get_random_piece_at_position(position)

        if grid.can_add_object(piece):
            grid.add_object(piece)
        else:
            raise GameOverException("New piece cannot be added to board!")

        return piece