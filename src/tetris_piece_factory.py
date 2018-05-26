"""Classes: TetrisPieceFactory."""

import random

from src.layouts import Layouts
from src.tetris_piece import TetrisPiece
from src.immutable import Immutable


class TetrisPieceFactory(Immutable):
    """Manufactures instances of TetrisPiece."""

    def __init__(self):   # noqa: D107
        super(TetrisPieceFactory, self).__init__()

    def get_random_piece_at_position(self, position):
        """Get a random TetrisPiece with given position."""
        return TetrisPiece(
            random.choice(Layouts.ALL),
            position
        )
