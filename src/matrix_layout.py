"""Classes: MatrixLayout."""

from src.layout import Layout
from src.position import Position


class MatrixLayout(Layout):
    """
    MatrixLayout provides an interface for constructing a Layout from a 2-dimension list (matrix) of 'truthy' values.

    The i, j indices of the matrix are mapped to Position objects used to construct the Layout.

    The purpose of MatrixLayout is to make it easy to construct a Layout from a pictorial representation in code.
    """

    def __init__(self, matrix):
        """
        Construct a Layout from the given matrix of 'truthy' values.

        See examples in Layouts class.
        """
        positions = []
        for i, col in enumerate(matrix):
            for j, cell in enumerate(col):
                if cell:
                    positions.append(Position(j, len(matrix) - i - 1))

        super(MatrixLayout, self).__init__(positions)
