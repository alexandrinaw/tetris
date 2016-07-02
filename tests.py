import unittest

from tetris import pieces, game_board


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


class BoardTest(unittest.TestCase):
    def test_remove_completed_lines_one_line(self):
        board = game_board.Board()

        # Fill in bottom row of board
        last_row_index = game_board.NUM_ROWS - 1
        for col_index in range(game_board.NUM_COLUMNS):
            block = pieces.Block(last_row_index, col_index, 3)
            board.array[last_row_index][col_index] = block

        board.remove_completed_lines()

        self.assertEqual(board.score, game_board.POINTS_PER_LINE)
        self.assertFalse(any(
            [any(board.array[row_index]) for row_index
             in range(game_board.NUM_ROWS)]))

    def test_remove_completed_lines_one_line_with_block_above(self):
        board = game_board.Board()

        # Fill in bottom row of board
        last_row_index = game_board.NUM_ROWS - 1
        for col_index in range(game_board.NUM_COLUMNS):
            block = pieces.Block(last_row_index, col_index, 3)
            board.array[last_row_index][col_index] = block
        # put in one extra block
        block = pieces.Block(last_row_index-1, col_index, 3)
        board.array[last_row_index-1][col_index] = block

        board.remove_completed_lines()

        self.assertEqual(board.score, game_board.POINTS_PER_LINE)
        self.assertTrue(any(
            [any(board.array[row_index]) for row_index
             in range(game_board.NUM_ROWS)]))
        # this is where that extra block should be after falling
        self.assertTrue(board.array[last_row_index][col_index])

    def test_new_shape(self):
        board = game_board.Board()
        board.start_game()

        board.new_shape()

        self.assertIsNotNone(board.falling_shape)
        self.assertIsNotNone(board.next_shape)

    def test_new_shape_cannot_be_placed(self):
        board = game_board.Board()
        board.start_game()
        board = _fill_in_board(board)

        with self.assertRaises(game_board.GameOverError):
            board.new_shape()

        self.assertIsNone(board.falling_shape)

    def test_drop_shape(self):
        board = game_board.Board()
        board.start_game()
        falling_shape = board.falling_shape

        board.drop_shape()

        self.assertNotEqual(falling_shape, board.falling_shape)

    def test_drop_shape_cannot_be_placed(self):
        board = game_board.Board()
        board.start_game()
        board = _fill_in_board(board)
        falling_shape = board.falling_shape

        with self.assertRaises(game_board.GameOverError):
            board.drop_shape()

        self.assertEqual(falling_shape, board.falling_shape)

    def test_move_shape_left_returns_true_if_successful(self):
        board = game_board.Board()
        board.start_game()

        self.assertTrue(board.move_shape_left())

    def test_move_shape_left_returns_false_if_not_successful(self):
        board = game_board.Board()
        board.start_game()
        board = _fill_in_board(board)

        self.assertFalse(board.move_shape_left())

    def test_move_shape_right_returns_true_if_successful(self):
        board = game_board.Board()
        board.start_game()

        self.assertTrue(board.move_shape_right())

    def test_move_shape_right_returns_false_if_not_successful(self):
        board = game_board.Board()
        board.start_game()
        board = _fill_in_board(board)

        self.assertFalse(board.move_shape_right())

    def test_rotate_shape_returns_true_if_successful(self):
        board = game_board.Board()
        board.start_game()

        self.assertTrue(board.rotate_shape())

    def test_rotate_shape_returns_false_if_not_successful(self):
        board = game_board.Board()
        board.start_game()
        board = _fill_in_board(board)

        self.assertFalse(board.rotate_shape())

    def test_move_shape_down_moves_shape_down_one_row(self):
        board = game_board.Board()
        board.start_game()

        self.assertTrue(board.let_shape_fall())
        self.assertEqual(board.falling_shape.row_position, 1)

    def test_move_shape_down_settles_shape(self):
        board = game_board.Board()
        board.start_game()
        bottom_blocks = board.falling_shape.bottom_blocks
        lowest_position = max([block.row_position for block in bottom_blocks])
        # make sure board is empty
        self.assertFalse(any(
            [any(board.array[row_index]) for row_index
             in range(game_board.NUM_ROWS)]))

        # move piece all the way down
        for _ in range(game_board.NUM_ROWS-lowest_position):
            board.let_shape_fall()

        # make sure new blocks exist in board
        self.assertTrue(any(
            [any(board.array[row_index]) for row_index
             in range(game_board.NUM_ROWS)]))

    def test_move_shape_down_ends_game_if_not_possible(self):
        board = game_board.Board()
        board.start_game()
        board = _fill_in_board(board)

        with self.assertRaises(game_board.GameOverError):
            self.assertFalse(board.let_shape_fall())


def _fill_in_board(board):
    # fill in the entire board
    for row_index in range(game_board.NUM_ROWS):
        for col_index in range(game_board.NUM_COLUMNS):
            block = pieces.Block(row_index, col_index, 3)
            board.array[row_index][col_index] = block
    return board
