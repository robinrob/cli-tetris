import random

from src.layouts import Layouts
from src.tetris_piece import TetrisPiece
from src.immutable import Immutable


class TetrisPieceFactory(Immutable):
    def __init__(self):
        super(TetrisPieceFactory, self).__init__()

    def get_random_piece_at_position(self, position):
        return TetrisPiece(
            random.choice(Layouts.ALL),
            position
        )

    