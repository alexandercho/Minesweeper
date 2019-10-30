import random

class DisplayBoard:
    def __init__(self, N):
        self.size = N
        self.covered_cell, self.mine, self.empty_cell = 'X', 'M', '.'
        self.flag = 'F'
        self.grid = [[self.covered_cell for i in range(N)] for j in range(N)]

    def change_cell(self, row, col, val):
        if val == 0:
            self.grid[row][col] = self.empty_cell
        elif val != -1:
            self.grid[row][col] = val
        else:
            self.grid[row][col] = self.mine

    def is_covered(self, row, col):
        return self.grid[row][col] == self.covered_cell

    def flag(self, row, col):
        self.grid[row][col] = self.flag

    def get_grid(self):
        return self.grid

    def __str__(self):
        space_size = len(str(self.size))
        display_string = ' ' + ' '*space_size
        col_header = 1
        for i in range(self.size):
            display_string += str(col_header) + ' ' +' '*(space_size - len(str(col_header)))
            col_header += 1
        display_string += '\n'

        row_header = 1
        for row in self.grid:
            display_string += str(row_header) + ' ' +' '*(space_size - len(str(row_header)))
            col_header = 1
            for col in row:
                display_string += str(col) + ' '*(space_size)
                col_header += 1
            display_string += '\n'
            row_header += 1
        return display_string
