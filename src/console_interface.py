"""Classes: ConsoleInterface."""

import sys

from src.movement_type import MovementType
from src.immutable import Immutable


class ConsoleInterface(Immutable):
    """ConsoleInterface presents a console interface to the user for input and rendering."""

    def __init__(self):   # noqa: D107
        super(ConsoleInterface, self).__init__()

    def get_player_move(self):
        """Prompt the user for input and return the corresponding MovementType."""
        raw_input = self._get_player_input()

        if raw_input is "a":
            return MovementType.LEFT
        elif raw_input is "d":
            return MovementType.RIGHT
        elif raw_input is "w":
            return MovementType.ROTATE_ANTICLOCKWISE
        elif raw_input is "s":
            return MovementType.ROTATE_CLOCKWISE
        elif raw_input is "":
            return MovementType.NONE

    def _get_player_input(self):
        allowed_inputs = ["a", "d", "w", "s", ""]
        raw_input = None
        while raw_input not in allowed_inputs:
            sys.stdout.write(f"Please choose from allowed inputs: {allowed_inputs}: ")
            raw_input = input()

        return raw_input

    def render_hello_message(self):
        """Display the welcome message for CLI Tetris."""
        self._clear()
        print("Welcome to Tetris!\n")

        raw_input = None
        while raw_input is not "":
            raw_input = self._get_input_key("Enter")

    def _get_input_key(self, key_label):
        sys.stdout.write(f"Please press {key_label} to start: ")
        return input()

    def render_grid(self, tetris_grid, clear=True):
        """Render the Tetris grid."""
        if clear:
            self._clear()

        display_contents = ""
        for column in tetris_grid.grid_squares:
            for grid_square in column:
                display_contents += str(grid_square)

            display_contents += "\n"

        print(display_contents)

    def render_game_over_message(self, grid):
        """Display the game over message."""
        self._clear()
        print("Game Over!\n")
        self.render_grid(grid, clear=False)

    def _clear(self):
        # pass
        print(chr(27) + "[2J")