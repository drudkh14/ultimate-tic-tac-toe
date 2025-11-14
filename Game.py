import Constants
from BigBoard import BigBoard

class Game:

    def __init__(self):
        self.board = BigBoard()
        self.turn = 'X'
        self.running = True
        self.game_started = False

    def handle_click(self, pos):
        big_row, big_col, small_row, small_col = self.get_cell(pos)

        success = self.board.make_move(big_row, big_col, small_row, small_col, self.turn)
        if success:
            self.turn = 'O' if self.turn == 'X' else 'X'

    @staticmethod
    def get_cell(pos):
        x, y = pos

        big_c = x // Constants.BIG_CELL_SIZE
        big_r = y // Constants.BIG_CELL_SIZE
        small_c = (x % Constants.BIG_CELL_SIZE) // (Constants.CELL_SIZE + Constants.GAP)
        small_r = (y % Constants.BIG_CELL_SIZE) // (Constants.CELL_SIZE + Constants.GAP)
        return int(big_r), int(big_c), int(small_r), int(small_c)

    def reset(self):
        self.board = BigBoard()
        self.turn = 'X'