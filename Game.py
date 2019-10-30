from GameBoard import *
from DisplayBoard import *

class Game:

    def __init__(self,N,M):
        self.N = N
        self.M = M
        self.gameboard = GameBoard(N,M)
        self.displayboard = DisplayBoard(N)
        self.num_uncovered = 0
        self.game_over = False
        self.game_won = False

    def is_win(self):
        return self.game_won

    def is_loss(self, row, col):
        return self.gameboard.is_mine(row,col)

    def play_move(self, row, col):
        uncovered_cells = self.gameboard.get_uncovered_cells(row,col)
        for cell in uncovered_cells:
            cell_row, cell_col = cell[0], cell[1]
            val = self.gameboard.get_cell(cell_row, cell_col)
            self.displayboard.change_cell(cell_row, cell_col, val)
        self.num_uncovered += len(uncovered_cells)

        if self.N**2 - self.M == self.num_uncovered:
            self.game_won = True
            self.game_over = True
        if self.is_loss(row, col):
            self.game_over = True

    def is_valid_move(self, row, col):
        return self.gameboard.in_grid(row,col) and self.displayboard.is_covered(row,col)

    def get_display(self):
        return self.displayboard.get_grid()

    def uncover_board(self):
        for i in range(self.N):
            for j in range(self.N):
                self.displayboard.change_cell(i, j, self.gameboard.get_cell(i, j))
