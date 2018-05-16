from src.layout import Layout
from src.position import Position


class MatrixLayout(Layout):
    def __init__(self, matrix):
        positions = []
        for i, col in enumerate(matrix):
            for j, cell in enumerate(col):
                print(i, j)
                if cell:
                    positions.append(Position(j, len(matrix) - i - 1))

        super(MatrixLayout, self).__init__(positions)
