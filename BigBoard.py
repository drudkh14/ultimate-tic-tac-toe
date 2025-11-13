from Constants import BIG_CELL_NUMBER
from MiniBoard import MiniBoard


class BigBoard:

    def __init__(self):
        self.boards = [[MiniBoard() for _ in range (BIG_CELL_NUMBER)] for _ in range(BIG_CELL_NUMBER)]
        self.global_winner = None
        self.active_board = None

    def make_move(self, big_row, big_col, small_row, small_col, player):
        mini_board = self.boards[big_row][big_col]

        if self.active_board and (big_row, big_col) != self.active_board:
            return False

        success = mini_board.make_move(small_row, small_col, player)

        self.update_active_board(small_row, small_col)
        self.update_global_winner()

        return success

    def update_active_board(self, small_row, small_col):
        next_board = self.boards[small_row][small_col]

        if next_board.winner or next_board.is_full():
            self.active_board = None
        else:
            self.active_board = (small_row, small_col)

    def update_global_winner(self):
        for i in range(3):
            if (self.boards[i][0].winner == self.boards[i][1].winner == self.boards[i][2].winner and
                    self.boards[i][0].winner):
                self.global_winner = self.boards[i][0].winner
                return
            if (self.boards[0][i].winner == self.boards[1][i].winner == self.boards[2][i].winner and
                    self.boards[0][i].winner):
                self.global_winner = self.boards[0][i].winner
                return

        if (self.boards[0][0].winner == self.boards[1][1].winner == self.boards[2][2].winner and
                self.boards[0][0].winner):
            self.global_winner = self.boards[0][0].winner
            return
        if (self.boards[0][2].winner == self.boards[1][1].winner == self.boards[2][0].winner and
                self.boards[0][2].winner):
            self.global_winner = self.boards[0][2].winner
            return

        if all(board.winner for row in self.boards for board in row):
            self.global_winner = 'D'