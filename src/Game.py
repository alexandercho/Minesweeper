from GameBoard import *
from DisplayBoard import *

class Game:

    def __init__(self,N,M):
        self.N = N
        self.M = M
        self.gameboard = GameBoard(N,M)
        self.displayboard = DisplayBoard(N)
        self.game_over = False
        self.game_won = False
        self.remaining_cells = []
        for i in range(N):
            for j in range(N):
                self.remaining_cells += [(i,j)]

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
            self.remaining_cells.remove(cell)

        if self.M == len(self.remaining_cells):
            self.game_won = True
            self.game_over = True
        if self.is_loss(row, col):
            self.game_over = True

    def neighbor_sum(self, row, col):
        n = 0
        for i in range(-1,2):
            for j in range(-1,2):
                adj_row, adj_col = row + i, col + j
                if self.gameboard.in_grid(adj_row, adj_col) and (abs(i) + abs(j) == 1):
                    if (adj_row, adj_col) not in self.remaining_cells and self.gameboard.get_cell(adj_row, adj_col) != -1:
                        n += 1
        return n
    def get_neighbors(self, row, col):
        n = []
        for i in range(-1,2):
            for j in range(-1,2):
                adj_row, adj_col = row + i, col + j
                if self.gameboard.in_grid(adj_row, adj_col) and (abs(i) + abs(j) == 1):
                    if (adj_row, adj_col) not in self.remaining_cells and self.gameboard.get_cell(adj_row, adj_col) != -1:
                        n += [(adj_row,adj_col,self.display.g)]
        return n
    def get_numbers(self):
        return self.displayboard.get_numbers()

    def is_valid_move(self, row, col):
        return self.gameboard.in_grid(row,col) and self.displayboard.is_covered(row,col)

    def get_display(self):
        return self.displayboard.get_grid()

    def uncover_board(self):
        for i in range(self.N):
            for j in range(self.N):
                self.displayboard.change_cell(i, j, self.gameboard.get_cell(i, j))
