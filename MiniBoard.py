from setuptools.config.pyprojecttoml import load_file

import Constants
from Cell import Cell
from Constants import SMALL_CELL_NUMBER


class MiniBoard:

    def __init__(self):
        self.cells = [[Cell() for _ in range(SMALL_CELL_NUMBER)] for _ in range(SMALL_CELL_NUMBER)]
        self.winner = None

    def make_move(self, row, col, player):
        if self.winner:
            return False

        cell = self.cells[row][col]

        if not cell.is_empty():
            return False

        cell.value = player

        self.update_winner()

        return True

    def update_winner(self):
        for i in range(3):
            if self.cells[i][0].value == self.cells[i][1].value == self.cells[i][2].value and self.cells[i][0]:
                self.winner = self.cells[i][0].value
                return
            if self.cells[0][i].value == self.cells[1][i].value == self.cells[2][i].value and self.cells[0][i]:
                self.winner = self.cells[0][i].value
                return

        if self.cells[0][0].value == self.cells[1][1].value == self.cells[2][2].value and self.cells[0][0].value:
            self.winner = self.cells[0][0].value
            return
        if self.cells[0][2].value == self.cells[1][1].value == self.cells[2][0].value and self.cells[0][2].value:
            self.winner = self.cells[0][2].value
            return

        if self.is_full():
            self.winner = 'D'


    def is_full(self):
        return all(cell.value for row in self.cells for cell in row)
