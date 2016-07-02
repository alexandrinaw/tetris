"""Tetris Pieces and mechanisms for manipulating them."""

from random import randint


class Block(object):
    """Represents one block in a tetris piece."""

    def __init__(self, row_position, column_position, color):
        self.row_position = row_position
        self.column_position = column_position
        self.color = color


class Shape(object):
    """The object representing a shape, including its position, orientation,
    color, and set of blocks it includes."""

    def __init__(self, column, row, color=None, orientation=None):
        self.column_position = column
        self.row_position = row
        self.color = color or self._get_random_color()
        if orientation is not None:
            self.orientation = orientation
        else:
            self.orientation = self._get_random_orientation()
        self.blocks = []
        self._initialize_blocks()

    def __eq__(self, other):
        return (self.row_position == other.row_position
                and self.column_position == other.column_position)

    def _get_random_orientation(self):
        return randint(0, self.number_of_orientations-1)

    @staticmethod
    def _get_random_color():
        return randint(1, 6)

    def _rotate(self, clockwise=True):
        rotate_amount = 1 if clockwise else -1
        self.orientation = (self.orientation + rotate_amount) % self.number_of_orientations
        self._rotate_blocks(self.orientation)

    @property
    def number_of_orientations(self):
        raise NotImplementedError

    @property
    def block_positions(self):
        """A dict of lists of the positions for each block in the Shape, for each orientation.

        Note: These are *relative* positions as compared to the base position of the current Shape.
        """
        raise NotImplementedError

    @property
    def bottom_blocks_for_orientations(self):
        """A dit of lists of the blocks on the bottom positions of the Shape, for each orientation."""
        bottom_blocks_for_orientation = {}
        for orientation in self.block_positions:
            bottom_blocks_for_orientation[orientation] = []
            for index, position in enumerate(self.block_positions[orientation]):
                if any([other_position[0] == position[0]
                        and other_position[1] > position[1]
                        for other_position in self.block_positions[orientation]]):
                    pass
                else:
                    bottom_blocks_for_orientation[orientation].append(self.blocks[index])
        return bottom_blocks_for_orientation

    @property
    def bottom_blocks(self):
        """The blocks currently on the bottom of the Shape."""
        return self.bottom_blocks_for_orientations[self.orientation]

    def _initialize_blocks(self):
        relative_block_positions = self.block_positions[self.orientation]
        self.blocks = [Block(self.row_position+diff[1],
                             self.column_position+diff[0],
                             self.color)
                       for diff in relative_block_positions]

    def _rotate_blocks(self, orientation):
        new_block_positions_diff = self.block_positions[orientation]
        for (index, diff) in enumerate(new_block_positions_diff):
            self.blocks[index].column_position = self.column_position + diff[0]
            self.blocks[index].row_position = self.row_position + diff[1]

    def lower_shape_by_one_row(self):
        """Moves shape down."""
        self._shift_by(columns=0, rows=1)

    def raise_shape_by_one_row(self):
        """Moves shape up."""
        self._shift_by(columns=0, rows=-1)

    def shift_shape_right_by_one_column(self):
        """Moves shape right."""
        self._shift_by(columns=1, rows=0)

    def shift_shape_left_by_one_column(self):
        """Moves shape left."""
        self._shift_by(columns=-1, rows=0)

    def _shift_by(self, columns, rows):
        self.column_position += columns
        self.row_position += rows
        for block in self.blocks:
            block.column_position += columns
            block.row_position += rows

    def move_to(self, column, row):
        """Move to given position and ensure orientation is correct."""
        self.column_position = column
        self.row_position = row
        self._rotate_blocks(self.orientation)

    def rotate_clockwise(self):
        """Rotate clockwise."""
        self._rotate(clockwise=True)

    def rotate_counterclockwise(self):
        """Rotate counterclockwise."""
        self._rotate(clockwise=False)

    @staticmethod
    def random(starting_column, starting_row):
        """Returns a randomly chosen piece at the given position."""
        rand = randint(0, 6)
        if rand == 0:
            new_piece = SquareShape(starting_column, starting_row)
        elif rand == 1:
            new_piece = LineShape(starting_column, starting_row)
        elif rand == 2:
            new_piece = SShape(starting_column, starting_row)
        elif rand == 3:
            new_piece = LShape(starting_column, starting_row)
        elif rand == 4:
            new_piece = TShape(starting_column, starting_row)
        elif rand == 5:
            new_piece = ZShape(starting_column, starting_row)
        elif rand == 6:
            new_piece = JShape(starting_column, starting_row)
        return new_piece


class SquareShape(Shape):
    """ Orientation:    0
        =====================
        Shape:      | 0*| 1 |
                    | 2 | 3 |

        * is the "base" location for the Shape. The block positions
          are offsets from this location.
    """
    @property
    def number_of_orientations(self):
        return 1

    @property
    def block_positions(self):
        return {
            0: [(0, 0), (1, 0), (0, 1), (1, 1)],
        }


class TShape(Shape):
    """ Orientation:    0           90              180               270
        ====================================================================
        Shape:      * | 0 |      * | 1 |          *                 * | 1 |
                  | 1 | 2 | 3 |    | 2 | 0 |    | 1 | 2 | 3 |     | 0 | 2 |
                                   | 3 |            | 0 |             | 3 |
    """
    @property
    def number_of_orientations(self):
        return 4

    @property
    def block_positions(self):
        return {
            0: [(1, 0), (0, 1), (1, 1), (2, 1)],
            1: [(2, 1), (1, 0), (1, 1), (1, 2)],
            2: [(1, 2), (0, 1), (1, 1), (2, 1)],
            3: [(0, 1), (1, 0), (1, 1), (1, 2)]
        }


class LineShape(Shape):
    """ Orientation:  0            90
        ======================================
        Shape:      | 0*|   | 0 | 1*| 2 | 3 |
                    | 1 |
                    | 2 |
                    | 3 |
    """
    @property
    def number_of_orientations(self):
        return 2

    @property
    def block_positions(self):
        return {
            0: [(0, 0), (0, 1), (0, 2), (0, 3)],
            1: [(-1, 0), (0, 0), (1, 0), (2, 0)],
        }


class SShape(Shape):
    """ Orientation:  0               90
        =====================================
        Shape:      | 0*|         * | 1 | 0 |
                    | 1 | 2 |   | 3 | 2 |
                        | 3 |
    """
    @property
    def number_of_orientations(self):
        return 2

    @property
    def block_positions(self):
        return {
            0: [(0, 0), (0, 1), (1, 1), (1, 2)],
            1: [(2, 0), (1, 0), (1, 1), (0, 1)],
        }


class ZShape(Shape):
    """ Orientation:  0               90
        =====================================
        Shape:        * | 0 |   | 0 | 1*|
                    | 2 | 1 |       | 2 | 3 |
                    | 3 |
    """
    @property
    def number_of_orientations(self):
        return 2

    @property
    def block_positions(self):
        return {
            0: [(1, 0), (1, 1), (0, 1), (0, 2)],
            1: [(-1, 0), (0, 0), (0, 1), (1, 1)],
        }


class LShape(Shape):
    """ Orientation:  0              90            180           270
        ====================================================================
        Shape:      | 0*|             *         | 3 | 2*|         * | 3 |
                    | 1 |       | 2 | 1 | 0 |       | 1 |   | 0 | 1 | 2 |
                    | 2 | 3 |   | 3 |               | 0 |
    """
    @property
    def number_of_orientations(self):
        return 4

    @property
    def block_positions(self):
        return {
            0: [(0, 0), (0, 1), (0, 2), (1, 2)],
            1: [(1, 1), (0, 1), (-1, 1), (-1, 2)],
            2: [(0, 2), (0, 1), (0, 0), (-1, 0)],
            3: [(-1, 1), (0, 1), (1, 1), (1, 0)]
        }


class JShape(Shape):
    """ Orientation:    0           90           180           270
        ====================================================================
        Shape:      * | 0 |   | 3*|           | 2*| 3 |   | 0*| 1 | 2 |
                      | 1 |   | 2 | 1 | 0 |   | 1 |               | 3 |
                  | 3 | 2 |                   | 0 |
    """
    @property
    def number_of_orientations(self):
        return 4

    @property
    def block_positions(self):
        return {
            0: [(1, 0), (1, 1), (1, 2), (0, 2)],
            1: [(2, 1), (1, 1), (0, 1), (0, 0)],
            2: [(0, 2), (0, 1), (0, 0), (1, 0)],
            3: [(0, 0), (1, 0), (2, 0), (2, 1)]
        }
