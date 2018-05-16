from src.position import Position
from src.layout import Layout
from settings import PIECE_SIZE


class Layouts:
    ALL = [
        # ****
        Layout([
            Position(-1, 0),
            Position(0, 0),
            Position(1, 0),
            Position(2, 0),
        ]).magnified(PIECE_SIZE),
        # *
        # *
        # **
        Layout([
            Position(0, 1),
            Position(0, 0),
            Position(0, -1),
            Position(1, -1),
        ]).magnified(PIECE_SIZE),
        #  *
        #  *
        # **
        Layout([
            Position(1, 1),
            Position(1, 0),
            Position(1, -1),
            Position(0, -1),
        ]).magnified(PIECE_SIZE),
        #  *
        # **
        # *
        Layout([
            Position(1, 1),
            Position(1, 0),
            Position(0, 0),
            Position(0, -1),
        ]).magnified(PIECE_SIZE),
        # * *
        # * *
        Layout([
            Position(0, 0),
            Position(0, 1),
            Position(1, 0),
            Position(1, 1),
        ]).magnified(PIECE_SIZE),
    ]

    # Maximum offset from (0, 0) of all possible layouts
    MAX_DIMENSION = max([
        max([
            max([pos.x for pos in layout.positions]),
            max([pos.y for pos in layout.positions])
        ]) for layout in ALL
    ])
