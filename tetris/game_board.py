import copy
import curses
import math

from tetris.pieces import Shape


NUM_COLUMNS = 10
NUM_ROWS = 20

STARTING_COLUMN = 4
STARTING_ROW = 0

PREVIEW_COLUMN = 12
PREVIEW_ROW = 1

BLOCK_WIDTH = 2
BORDER_WIDTH = 1

POINTS_PER_LINE = 20
POINTS_PER_LEVEL = 200


class Board(object):
    """Maintains the entire state of the game."""
    def __init__(self, columns=None, rows=None, level=None):
        self.num_rows = rows or NUM_ROWS
        self.num_columns = columns or NUM_COLUMNS
        self.array = [[None for _ in range(self.num_columns)] for _ in range(self.num_rows)]
        self.falling_shape = None
        self.next_shape = None
        self.score = 0
        self.level = level or 1

    def start_game(self):
        self.score = 0
        self.level = 1
        if self.next_shape is None:
            self.next_shape = Shape.random(PREVIEW_COLUMN, PREVIEW_ROW)
            self.new_shape()

    def end_game(self):
        raise GameOverError(score=self.score, level=self.level)

    def new_shape(self):
        self.falling_shape = self.next_shape
        self.falling_shape.move_to(STARTING_COLUMN, STARTING_ROW)
        self.next_shape = Shape.random(PREVIEW_COLUMN, PREVIEW_ROW)
        if self.shape_cannot_be_placed(self.falling_shape):
            self.next_shape = self.falling_shape
            self.falling_shape = None
            self.next_shape.move_to(PREVIEW_COLUMN, PREVIEW_ROW)
            self.end_game()

    def remove_completed_lines(self):
        rows_removed = []
        lowest_row_removed = 0
        for row in self.array:
            if all(row):
                lowest_row_removed = max(lowest_row_removed, row[0].row_position)
                rows_removed.append(copy.deepcopy(row))
                for block in row:
                    self.array[block.row_position][block.column_position] = None
        if len(rows_removed) > 0:
            points_earned = math.pow(2, len(rows_removed)-1) * POINTS_PER_LINE
            self.score += points_earned
            if self.score > POINTS_PER_LEVEL * self.level:
                self.level += 1

            for column_index in range(0, NUM_COLUMNS):
                for row_index in range(lowest_row_removed, 0, -1):
                    block = self.array[row_index][column_index]
                    if block:
                        # number of rows removed that were below this one
                        distance_to_drop = len(
                            [row for row in rows_removed if
                             row[0].row_position > block.row_position]
                        )
                        new_row_index = row_index + distance_to_drop
                        self.array[row_index][column_index] = None
                        self.array[new_row_index][column_index] = block
                        block.row_position = new_row_index

    def settle_falilng_shape(self):
        """Resolves the current falling shape."""
        if self.falling_shape:
            self._settle_shape(self.falling_shape)
            self.falling_shape = None
            self.new_shape()

    def _settle_shape(self, shape):
        """Adds shape to settled pieces array."""
        if shape:
            for block in shape.blocks:
                self.array[block.row_position][block.column_position] = block
        self.remove_completed_lines()

    def move_shape_left(self):
        """When the user hits the left arrow."""
        if self.falling_shape:
            self.falling_shape.shift_shape_left_by_one_column()
            if self.shape_cannot_be_placed(self.falling_shape):
                self.falling_shape.shift_shape_right_by_one_column()
                return False
            return True

    def move_shape_right(self):
        """When the user hits the right arrow."""
        if self.falling_shape:
            self.falling_shape.shift_shape_right_by_one_column()
            if self.shape_cannot_be_placed(self.falling_shape):
                self.falling_shape.shift_shape_left_by_one_column()
                return False
            return True

    def rotate_shape(self):
        """When the user hits the up arrow."""
        if self.falling_shape:
            self.falling_shape.rotate_clockwise()
            if self.shape_cannot_be_placed(self.falling_shape):
                self.falling_shape.rotate_counterclockwise()
                return False
            return True

    def let_shape_fall(self):
        """What happens during every `tick`. Also what happens when the user hits down arrow."""
        if self.falling_shape:
            self.falling_shape.lower_shape_by_one_row()
            if self.shape_cannot_be_placed(self.falling_shape):
                self.falling_shape.raise_shape_by_one_row()
                if self.shape_cannot_be_placed(self.falling_shape):
                    self.end_game()
                else:
                    self.settle_falilng_shape()
            return True

    def drop_shape(self):
        """When you hit the enter arrow and the piece goes all the way down."""
        if self.falling_shape:
            while not self.shape_cannot_be_placed(self.falling_shape):
                self.falling_shape.lower_shape_by_one_row()
            self.falling_shape.raise_shape_by_one_row()
            if self.shape_cannot_be_placed(self.falling_shape):
                self.end_game()
            else:
                self.settle_falilng_shape()
            return True

    def shape_cannot_be_placed(self, shape):
        for block in shape.blocks:
            if (block.column_position < 0 or
                    block.column_position >= NUM_COLUMNS or
                    block.row_position < 0 or
                    block.row_position >= NUM_ROWS or
                    self.array[block.row_position][block.column_position] is not None):
                return True
        return False


class BoardDrawer(object):
    def __init__(self):
        stdscr = curses.initscr()
        stdscr.nodelay(1)
        curses.start_color()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_RED)
        curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLUE)
        curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_GREEN)
        curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_MAGENTA)
        curses.init_pair(5, curses.COLOR_CYAN, curses.COLOR_CYAN)
        curses.init_pair(6, curses.COLOR_YELLOW, curses.COLOR_YELLOW)
        curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(8, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair(10, 10, 10)
        curses.cbreak()
        stdscr.keypad(1)
        curses.nonl()
        curses.curs_set(0)
        curses.noecho()
        self.stdscr = stdscr

    def update_falling_piece(self, board):
        """Adds the currently falling pieces to the next stdscr to be drawn."""
        # actual game board: falling piece
        if board.falling_shape:
            for block in board.falling_shape.blocks:
                self.stdscr.addstr(
                    block.row_position+BORDER_WIDTH,
                    BLOCK_WIDTH*block.column_position+BORDER_WIDTH,
                    ' '*BLOCK_WIDTH,
                    curses.color_pair(block.color)
                )

    def update_settled_pieces(self, board):
        """Adds the already settled pieces to the next stdscr to be drawn."""
        # actual game board: settled pieces
        for (r_index, row) in enumerate(board.array):
            for (c_index, value) in enumerate(row):
                block = value
                if block:
                    color_pair = block.color
                else:
                    color_pair = 0
                self.stdscr.addstr(
                    r_index+BORDER_WIDTH,
                    c_index*BLOCK_WIDTH+BORDER_WIDTH,
                    ' '*BLOCK_WIDTH,
                    curses.color_pair(color_pair)
                )

    def update_shadow(self, board):
        """Adds the 'shadow' of the falling piece to the next stdscr to be drawn."""
        # where this piece will land
        shadow = copy.deepcopy(board.falling_shape)
        if shadow:
            while not board.shape_cannot_be_placed(shadow):
                shadow.lower_shape_by_one_row()
            shadow.raise_shape_by_one_row()
            for block in shadow.blocks:
                self.stdscr.addstr(
                    block.row_position+BORDER_WIDTH,
                    BLOCK_WIDTH*block.column_position+BORDER_WIDTH,
                    ' '*BLOCK_WIDTH,
                    curses.color_pair(8))

    def update_next_piece(self, board):
        """Adds the next piece to the next stdscr to be drawn."""
        # next piece
        if board.next_shape:
            for preview_row_offset in range(4):
                self.stdscr.addstr(
                    PREVIEW_ROW+preview_row_offset+BORDER_WIDTH,
                    (PREVIEW_COLUMN-1)*BLOCK_WIDTH+BORDER_WIDTH*2,
                    '    '*BLOCK_WIDTH,
                    curses.color_pair(0)
                )
            for block in board.next_shape.blocks:
                self.stdscr.addstr(
                    block.row_position+BORDER_WIDTH,
                    block.column_position*BLOCK_WIDTH+BORDER_WIDTH*2,
                    ' '*BLOCK_WIDTH,
                    curses.color_pair(block.color)
                )

    def update_score_and_level(self, board):
        """Adds the score and level to the next stdscr to be drawn."""
        # level
        self.stdscr.addstr(
            5+BORDER_WIDTH,
            PREVIEW_COLUMN*BLOCK_WIDTH-2+BORDER_WIDTH,
            'LEVEL: %d' % board.level,
            curses.color_pair(7)
        )
        # score
        self.stdscr.addstr(
            6+BORDER_WIDTH,
            PREVIEW_COLUMN*BLOCK_WIDTH-2+BORDER_WIDTH,
            'SCORE: %d' % board.score,
            curses.color_pair(7)
        )

    def clear_score(self):
        # level
        self.stdscr.addstr(
            5+BORDER_WIDTH,
            PREVIEW_COLUMN*BLOCK_WIDTH-2+BORDER_WIDTH,
            'LEVEL:              ',
            curses.color_pair(7)
        )
        # score
        self.stdscr.addstr(
            6+BORDER_WIDTH,
            PREVIEW_COLUMN*BLOCK_WIDTH-2+BORDER_WIDTH,
            'SCORE:              ',
            curses.color_pair(7)
        )

    def update_border(self):
        """Adds the border to the next stdscr to be drawn."""
        # side borders
        for row_position in range(NUM_ROWS+BORDER_WIDTH*2):
            self.stdscr.addstr(row_position, 0, '|', curses.color_pair(7))
            self.stdscr.addstr(row_position, NUM_COLUMNS*BLOCK_WIDTH+1, '|', curses.color_pair(7))
        # top and bottom borders
        for column_position in range(NUM_COLUMNS*BLOCK_WIDTH+BORDER_WIDTH*2):
            self.stdscr.addstr(0, column_position, '-', curses.color_pair(7))
            self.stdscr.addstr(NUM_ROWS+1, column_position, '-', curses.color_pair(7))

    def update(self, board):
        """Updates all visual board elements and then refreshes the screen."""
        self.update_border()
        self.update_score_and_level(board)
        self.update_next_piece(board)

        self.update_settled_pieces(board)

        self.update_falling_piece(board)
        self.update_shadow(board)

        self.refresh_screen()

    def refresh_screen(self):
        """Re-draws the current screen."""
        stdscr = self.stdscr
        stdscr.refresh()

    @staticmethod
    def return_screen_to_normal():
        """Undoes the weird settings to the terminal isn't screwed up when the game is over"""
        curses.endwin()


class GameOverError(Exception):
    def __init__(self, score, level):
        super(GameOverError).__init__(GameOverError)
        self.score = score
        self.level = level
