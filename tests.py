import unittest

from tetris import pieces


class ZShapeTests(unittest.TestCase):
    def test_rotation(self):
        shape = pieces.ZShape(0, 0, orientation=0)

        self.assertEqual(0, shape.orientation)
        self.assertEqual(
            [(1, 0), (1, 1), (0, 1), (0, 2)],
            shape.block_positions[shape.orientation])
        self.assertEqual(2, len(shape.bottom_blocks))

        shape.rotate_clockwise()

        self.assertEqual(1, shape.orientation)
        self.assertEqual(
            [(-1, 0), (0, 0), (0, 1), (1, 1)],
            shape.block_positions[shape.orientation])
        self.assertEqual(3, len(shape.bottom_blocks))

        shape.rotate_clockwise()

        self.assertEqual(0, shape.orientation)
        self.assertEqual(
            [(1, 0), (1, 1), (0, 1), (0, 2)],
            shape.block_positions[shape.orientation])
        self.assertEqual(2, len(shape.bottom_blocks))


class SShapeTests(unittest.TestCase):
    def test_rotation(self):
        shape = pieces.SShape(0, 0, orientation=0)

        self.assertEqual(0, shape.orientation)
        self.assertEqual(
            [(0, 0), (0, 1), (1, 1), (1, 2)],
            shape.block_positions[shape.orientation])
        self.assertEqual(2, len(shape.bottom_blocks))

        shape.rotate_clockwise()

        self.assertEqual(1, shape.orientation)
        self.assertEqual(
            [(2, 0), (1, 0), (1, 1), (0, 1)],
            shape.block_positions[shape.orientation])
        self.assertEqual(3, len(shape.bottom_blocks))

        shape.rotate_clockwise()

        self.assertEqual(0, shape.orientation)
        self.assertEqual(
            [(0, 0), (0, 1), (1, 1), (1, 2)],
            shape.block_positions[shape.orientation])
        self.assertEqual(2, len(shape.bottom_blocks))


class LShapeTests(unittest.TestCase):
    def test_rotation(self):
        shape = pieces.LShape(0, 0, orientation=0)

        self.assertEqual(0, shape.orientation)
        self.assertEqual(
            [(0, 0), (0, 1), (0, 2), (1, 2)],
            shape.block_positions[shape.orientation])
        self.assertEqual(2, len(shape.bottom_blocks))

        shape.rotate_clockwise()

        self.assertEqual(1, shape.orientation)
        self.assertEqual(
            [(1, 1), (0, 1), (-1, 1), (-1, 2)],
            shape.block_positions[shape.orientation])
        self.assertEqual(3, len(shape.bottom_blocks))

        shape.rotate_clockwise()

        self.assertEqual(2, shape.orientation)
        self.assertEqual(
            [(0, 2), (0, 1), (0, 0), (-1, 0)],
            shape.block_positions[shape.orientation])
        self.assertEqual(2, len(shape.bottom_blocks))

        shape.rotate_clockwise()

        self.assertEqual(3, shape.orientation)
        self.assertEqual(
            [(-1, 1), (0, 1), (1, 1), (1, 0)],
            shape.block_positions[shape.orientation])
        self.assertEqual(3, len(shape.bottom_blocks))

        shape.rotate_clockwise()

        self.assertEqual(0, shape.orientation)
        self.assertEqual(
            [(0, 0), (0, 1), (0, 2), (1, 2)],
            shape.block_positions[shape.orientation])
        self.assertEqual(2, len(shape.bottom_blocks))


class JShapeTests(unittest.TestCase):
    def test_rotation(self):
        shape = pieces.JShape(0, 0, orientation=0)

        self.assertEqual(0, shape.orientation)
        self.assertEqual(
            [(1, 0), (1, 1), (1, 2), (0, 2)],
            shape.block_positions[shape.orientation])
        self.assertEqual(2, len(shape.bottom_blocks))

        shape.rotate_clockwise()

        self.assertEqual(1, shape.orientation)
        self.assertEqual(
            [(2, 1), (1, 1), (0, 1), (0, 0)],
            shape.block_positions[shape.orientation])
        self.assertEqual(3, len(shape.bottom_blocks))

        shape.rotate_clockwise()

        self.assertEqual(2, shape.orientation)
        self.assertEqual(
            [(0, 2), (0, 1), (0, 0), (1, 0)],
            shape.block_positions[shape.orientation])
        self.assertEqual(2, len(shape.bottom_blocks))

        shape.rotate_clockwise()

        self.assertEqual(3, shape.orientation)
        self.assertEqual(
            [(0, 0), (1, 0), (2, 0), (2, 1)],
            shape.block_positions[shape.orientation])
        self.assertEqual(3, len(shape.bottom_blocks))

        shape.rotate_clockwise()

        self.assertEqual(0, shape.orientation)
        self.assertEqual(
            [(1, 0), (1, 1), (1, 2), (0, 2)],
            shape.block_positions[shape.orientation])
        self.assertEqual(2, len(shape.bottom_blocks))


class TShapeTests(unittest.TestCase):
    def test_rotation(self):
        shape = pieces.TShape(0, 0, orientation=0)

        self.assertEqual(0, shape.orientation)
        self.assertEqual(
            [(1, 0), (0, 1), (1, 1), (2, 1)],
            shape.block_positions[shape.orientation])
        self.assertEqual(3, len(shape.bottom_blocks))

        shape.rotate_clockwise()

        self.assertEqual(1, shape.orientation)
        self.assertEqual(
            [(2, 1), (1, 0), (1, 1), (1, 2)],
            shape.block_positions[shape.orientation])
        self.assertEqual(2, len(shape.bottom_blocks))

        shape.rotate_clockwise()

        self.assertEqual(2, shape.orientation)
        self.assertEqual(
            [(1, 2), (0, 1), (1, 1), (2, 1)],
            shape.block_positions[shape.orientation])
        self.assertEqual(3, len(shape.bottom_blocks))

        shape.rotate_clockwise()

        self.assertEqual(3, shape.orientation)
        self.assertEqual(
            [(0, 1), (1, 0), (1, 1), (1, 2)],
            shape.block_positions[shape.orientation])
        self.assertEqual(2, len(shape.bottom_blocks))

        shape.rotate_clockwise()

        self.assertEqual(0, shape.orientation)
        self.assertEqual(
            [(1, 0), (0, 1), (1, 1), (2, 1)],
            shape.block_positions[shape.orientation])
        self.assertEqual(3, len(shape.bottom_blocks))


class SquareShapeTests(unittest.TestCase):
    def test_rotation(self):
        shape = pieces.SquareShape(0, 0, orientation=0)

        self.assertEqual(0, shape.orientation)
        self.assertEqual(
            [(0, 0), (1, 0), (0, 1), (1, 1)],
            shape.block_positions[shape.orientation])
        self.assertEqual(2, len(shape.bottom_blocks))

        shape.rotate_clockwise()

        self.assertEqual(0, shape.orientation)
        self.assertEqual(
            [(0, 0), (1, 0), (0, 1), (1, 1)],
            shape.block_positions[shape.orientation])
        self.assertEqual(2, len(shape.bottom_blocks))


class LineShapeTests(unittest.TestCase):
    def test_rotation(self):
        shape = pieces.LineShape(0, 0, orientation=0)

        self.assertEqual(0, shape.orientation)
        self.assertEqual(
            [(0, 0), (0, 1), (0, 2), (0, 3)],
            shape.block_positions[shape.orientation])
        self.assertEqual(1, len(shape.bottom_blocks))

        shape.rotate_clockwise()

        self.assertEqual(1, shape.orientation)
        self.assertEqual(
            [(-1, 0), (0, 0), (1, 0), (2, 0)],
            shape.block_positions[shape.orientation])
        self.assertEqual(4, len(shape.bottom_blocks))

        shape.rotate_clockwise()

        self.assertEqual(0, shape.orientation)
        self.assertEqual(
            [(0, 0), (0, 1), (0, 2), (0, 3)],
            shape.block_positions[shape.orientation])
        self.assertEqual(1, len(shape.bottom_blocks))


class ShapeMovementTest(unittest.TestCase):
    def test_lower_shape(self):
        shape = pieces.Shape.random(2, 2)

        shape.lower_shape_by_one_row()

        self.assertEqual(shape.row_position, 3)
        self.assertEqual(shape.column_position, 2)

    def test_raise_shape(self):
        shape = pieces.Shape.random(2, 2)

        shape.raise_shape_by_one_row()

        self.assertEqual(shape.row_position, 1)
        self.assertEqual(shape.column_position, 2)

    def test_move_shape_right(self):
        shape = pieces.Shape.random(2, 2)

        shape.shift_shape_right_by_one_column()

        self.assertEqual(shape.row_position, 2)
        self.assertEqual(shape.column_position, 3)

    def test_move_shape_left(self):
        shape = pieces.Shape.random(2, 2)

        shape.shift_shape_left_by_one_column()

        self.assertEqual(shape.row_position, 2)
        self.assertEqual(shape.column_position, 1)
