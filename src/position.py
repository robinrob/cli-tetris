import math


class Position:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"x: {self.x}, y: {self.y}"

    def translated(self, x, y):
        return Position(self.x + x, self.y + y)

    def relative_to(self, other_point):
        return Position(self.x - other_point.x, self.y - other_point.y)

    def rotated_around_origin(self, degrees):
        rad = math.pi / 180 * degrees

        return Position(
            self.x * math.cos(rad) - self.y * math.sin(rad),
            self.x * math.sin(rad) + self.y * math.cos(rad)
        )

    def rotated_around(self, degrees, pivot_pos):
        rel_pos = self.relative_to(pivot_pos)
        new_rel_pos = rel_pos.rotate_around_origin(degrees)

        return Position(
            new_rel_pos.x + pivot_pos.x,
            new_rel_pos.y + pivot_pos.y
        )

    def rounded(self, places=0):
        return Position(round(self.x, places), round(self.y, places))