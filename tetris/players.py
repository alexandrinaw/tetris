import copy
import logging

logging.basicConfig(filename='test.log', level=logging.DEBUG)


class Human(object):
    def __init__(self):
        self.name = 'Alex'


class AI(object):

    def __init__(self, weights=None):
        self.weights = weights or (-8, -18, -10.497, 16.432)

    def score_board(self, original_board, this_board):
        height_sum = get_height_sum(this_board)
        holes = get_holes(this_board)
        cumulative_holes = get_number_of_squares_above_holes(this_board)
        score_diff = this_board.score - original_board.score

        A, B, C, D = self.weights
        score = (
            (A * height_sum) +
            (B * holes) +
            (C * cumulative_holes) +
            (D * score_diff)
        )
        return score

    def get_moves(self, game_board, fun):
        max_score = -100000
        best_final_position = None
        falling_orientations = game_board.falling_shape.number_of_orientations
        next_orientations = game_board.next_shape.number_of_orientations
        for column_position in range(10):
            for orientation in range(falling_orientations):
                board = copy.deepcopy(game_board)
                falling_piece = board.falling_shape
                falling_piece.orientation = orientation
                falling_piece.move_to(column_position, 2)
                if board.shape_cannot_be_placed(falling_piece):
                    break
                fun.update_settled_pieces(board)  # clears out the old shadow locations
                fun.update_falling_piece(game_board)
                fun.update_shadow(board)
                fun.refresh_screen()
                if board.shape_cannot_be_placed(falling_piece):
                    break

                while not board.shape_cannot_be_placed(falling_piece):
                    falling_piece.lower_shape_by_one_row()
                falling_piece.raise_shape_by_one_row()
                board._settle_shape(falling_piece)
                for next_column_position in range(10):
                    for next_orientation in range(next_orientations):
                        falling_piece.color = 10
                        board2 = copy.deepcopy(board)
                        next_piece = board2.next_shape
                        board2.falling_shape = board2.next_shape
                        next_piece.orientation = next_orientation
                        next_piece.move_to(next_column_position, 2)
                        if board2.shape_cannot_be_placed(next_piece):
                            break
                        while not board2.shape_cannot_be_placed(next_piece):
                            next_piece.lower_shape_by_one_row()
                        next_piece.raise_shape_by_one_row()
                        board2._settle_shape(next_piece)

                        score = self.score_board(game_board, board2)
                        if score > max_score:
                            max_score = score
                            best_final_position = falling_piece

        return best_final_position


def get_holes(this_board):
    hole_count = 0
    for row in this_board.array:
        for cell in row:
            if cell and not _cell_below_is_occupied(cell, this_board.array):
                hole_count += 1
    return hole_count


def get_number_of_squares_above_holes(this_board):
    count = 0
    for column in range(this_board.num_columns):
        saw_hole = False
        for row in range(this_board.num_rows-1, 0, -1):
            cell = this_board.array[row][column]
            if cell:
                if saw_hole:
                    count += 1
            else:
                saw_hole = True
    return count


def _cell_below_is_occupied(cell, board):
    try:
        return board[cell.row_position + 1][cell.column_position]
    except IndexError:
        return True


def get_height_sum(this_board):
    return sum([20 - val.row_position for row in this_board.array for val in row if val])
