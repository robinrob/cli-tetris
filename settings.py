"""Contains runtime settings for CLI Tetris."""

import inspect
import os

PROJECT_ROOT = os.path.dirname(
    os.path.abspath(
        inspect.getfile(
            inspect.currentframe()
        )
    )
)

GRID_SIZE = 20

MOVE_UNITS = 1

PIECE_SIZE = 1