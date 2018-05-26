"""Classes: Layouts."""

from src.matrix_layout import MatrixLayout
from settings import PIECE_SIZE


class Layouts:
    """Layouts is a dictionary of possible TetrisPiece layouts."""

    L_LAYOUT_RIGHT = MatrixLayout([
        [1, 0],
        [1, 0],
        [1, 1]
    ])
    ALL = [
        MatrixLayout([
            [1, 1, 1, 1]
        ]),
        L_LAYOUT_RIGHT,
        L_LAYOUT_RIGHT.flipped_horizontally(),
        MatrixLayout([
            [0, 1],
            [1, 1],
            [1, 0]
        ]),
        MatrixLayout([
            [1, 1],
            [1, 1]
        ]),
        MatrixLayout([
            [0, 1, 0],
            [1, 1, 1],
            [0, 1, 0]
        ])
    ]
    ALL = [l.magnified(PIECE_SIZE) for l in ALL]

    # Maximum offset from (0, 0) of all possible layouts
    MAX_DIMENSION = max([
        max([
            max([abs(pos.x) for pos in layout.positions]),
            max([abs(pos.y) for pos in layout.positions])
        ]) for layout in ALL
    ]) + 1
