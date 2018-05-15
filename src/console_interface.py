from src.movement_type import MovementType

class ConsoleInterface:
    def get_player_move(self):
        if raw_input is "a":
            return MovementType.LEFT
        elif raw_input is "d":
            return MovementType.RIGHT
        elif raw_input is "w":
            return MovementType.ROTATE_ANTICLOCKWISE,
        elif raw_input is "s":
            return MovementType.ROTATE_CLOCKWISE

    def _get_player_input(self):
        allowed_inputs = ["a", "d", "w", "s"]
        raw_input = None
        while raw_input not in allowed_inputs:
            print(f"Please choose from allowed inputs: {allowed_inputs}:\n")
            raw_input = input()
        
        return raw_input

    def render_grid(self, tetris_grid):
        display = ""
        for column in tetris_grid.grid_squares:
            for grid_square in column:
                display += str(grid_square)
                
            display += "\n"

        print(display)
