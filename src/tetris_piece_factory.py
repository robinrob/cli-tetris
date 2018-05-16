import random

from src.position import Position
from src.layout import Layout
from src.tetris_piece import TetrisPiece


class TetrisPieceFactory:
    LAYOUTS = [
        # Layout([Position(0, 0)])
        # ****
        Layout([
            Position(-1, 0),
            Position(0, 0),
            Position(1, 0),
            Position(2, 0),
        ]),
        # *
        # *
        # **
        Layout([
            Position(0, 1),
            Position(0, 0),
            Position(0, -1),
            Position(1, -1),
        ]),
        #  *
        #  *
        # **
        Layout([
            Position(1, 1),
            Position(1, 0),
            Position(1, -1),
            Position(0, -1),
        ]),
        #  *
        # **
        # *
        Layout([
            Position(1, 1),
            Position(1, 0),
            Position(0, 0),
            Position(0, -1),
        ]),
        # * *
        # * *
        Layout([
            Position(0, 0),
            Position(0, 1),
            Position(1, 0),
            Position(1, 1),
        ])
    ]

    # Maximum offset from (0, 0) of all possible layouts
    MAX_DIMENSION = max([
        max([
            max([pos.x for pos in layout.positions]),
            max([pos.y for pos in layout.positions])
        ]) for layout in LAYOUTS
    ])

    def get_random_piece_at_position(self, position):
        return TetrisPiece(random.choice(TetrisPieceFactory.LAYOUTS), position)
