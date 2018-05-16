import unittest

from position import Position


class PositionTestCase(unittest.TestCase):
    def test_points_should_be_equal_when_coordinates_are_equal(self):
        pos1 = Position(3, 4)
        pos2 = Position(3, 4)

        self.assertEquals(pos1, pos2)

    def test_should_translate_by_0_0(self):
        pos = Position(4, 5)

        new_pos = pos.translated(0, 0)

        self.assertEquals(Position(4, 5), new_pos)

    def test_should_translate_by_3_2(self):
        pos = Position(4, 5)

        new_pos = pos.translated(3, 2)

        self.assertEquals(Position(7, 7), new_pos)

    def test_should_translate_by_minus_3_minus_2(self):
        pos = Position(1, 2)

        new_pos = pos.translated(-3, -2)

        self.assertEquals(Position(-2, 0), new_pos)

    def test_should_calculate_position_relative_to_other_point(self):
        pos = Position(4, 12)
        other_pos = Position(10, 10)

        relative_pos = pos.relative_to(other_pos)

        self.assertEquals(Position(-6, 2), relative_pos)

    def test_should_rotate_clockwise_by_90_degrees(self):
        pos = Position(0, 1)

        rotated_pos = pos.rotated(-90)

        self.assertEquals(Position(1, 0), rotated_pos.rounded())

    def test_should_rotate_by_180_degrees(self):
        pos = Position(0, 1)

        rotated_pos = pos.rotated(-180)

        self.assertEquals(Position(0, -1), rotated_pos.rounded())

    def test_should_rotate_clockwise_by_360_degrees(self):
        pos = Position(0, 1)

        rotated_pos = pos.rotated(360)

        self.assertEquals(Position(0, 1), rotated_pos.rounded())

    def test_should_rotate_anticlockwise_by_90_degrees(self):
        pos = Position(0, 1)

        rotated_pos = pos.rotated(90)

        self.assertEquals(Position(-1, 0), rotated_pos.rounded())

    def test_should_add_to_other_point(self):
        pos = Position(4, 5)
        other_pos = Position(6, 7)

        result = pos.add(other_pos)

        self.assertEquals(Position(10, 12), result)

    def test_should_return_dot_product_with_other_point(self):
        pos = Position(9, 12)
        other_pos = Position(2, -3)

        dot_product = pos.dot_product(other_pos)

        self.assertEquals(Position(18, -36), dot_product)