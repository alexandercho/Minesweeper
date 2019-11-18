import random

class Game(object):

    def __init__(self,N,M):
        self.N = N
        self.M = M
        self._game_grid = [[0 for i in range(self.N)] for j in range(self.N)]
        self.__generate_game_grid()
        self._game_over = False
        self._game_won = False

        self.covered_cell, self.mine, self.empty_cell = 'X', 'M', '.'
        self.display_grid = [[self.covered_cell for i in range(N)] for j in range(N)]

        self.remaining_cells = [(i//N, i%N) for i in range(N**2)]

    def is_win(self):
        return self._game_won

    def is_over(self):
        return self._game_over

    def play_move(self, cell):
        if self.__is_mine(cell):
            self.__uncover_cell(cell)
            self._game_over = True
        else:
            uncovered_cells = self.__get_uncovered_cells(cell)
            for u_cell in uncovered_cells:
                self.__uncover_cell(u_cell)
                self.remaining_cells.remove(u_cell)
            if self.M == len(self.remaining_cells):
                self._game_won = True
                self._game_over = True

    def is_valid_move(self, cell):
        return self.__in_grid(cell) and self.__is_covered(cell)

    def uncovered_numbers(self):
        un = []
        for i in range(self.N):
            for j in range(self.N):
                if self.display_grid[i][j] not in [self.covered_cell, self.mine, self.empty_cell]:
                    un.append((i, j, self.__get_cell((i, j)) ))
        return un

    def __generate_game_grid(self):
        mines = self.__get_mines()
        for mine in mines:
            self.__set_grid(mine, -1)
            for adj_cell in self.get_adj_cells(mine):
                if adj_cell not in mines:
                    self.__set_grid(adj_cell, self.__get_cell(adj_cell)+1)

    def __get_mines(self):
        mines = set((i//self.N, i%self.N) for i in range(self.N**2))
        return random.sample(mines, self.M)

    def __is_mine(self, cell):
        return self.__get_cell(cell) == -1

    def __get_cell(self, cell):
        return self._game_grid[cell[0]][cell[1]]

    def __set_grid(self, cell, val):
        self._game_grid[cell[0]][cell[1]] = val

    def __in_grid(self, cell):
        row, col = cell[0], cell[1]
        return (row >= 0) and (row < self.N) and (col >= 0) and (col < self.N)

    def get_adj_cells(self, cell):
        adj_cells = []
        row, col = cell[0], cell[1]
        for i in range(-1,2):
            for j in range(-1,2):
                adj_cell = (row + i, col + j)
                if abs(i) + abs(j) != 0 and self.__in_grid(adj_cell):
                    adj_cells.append(adj_cell)
        return adj_cells

    def __get_uncovered_cells(self, cell):
        if self.__is_mine(cell):
            return [cell]
        queue = [cell]
        uncovered_cells = []
        while queue:
            curr_cell = queue.pop(0)
            uncovered_cells.append(curr_cell)
            for adj_cell in self.get_adj_cells(curr_cell):
                if not (self.__is_mine(adj_cell) or adj_cell in uncovered_cells
                        or adj_cell in queue):
                    queue.append(adj_cell)
        return uncovered_cells

    def __uncover_cell(self, cell):
        row, col, val = cell[0], cell[1], self.__get_cell(cell)
        if val == 0:
            self.display_grid[row][col] = self.empty_cell
        elif val != -1:
            self.display_grid[row][col] = val
        else:
            self.display_grid[row][col] = self.mine

    def __is_covered(self, cell):
        return self.display_grid[cell[0]][cell[1]] == self.covered_cell

    def __str__(self):
        space_size = len(str(self.N))
        display_string = ' ' + ' '*space_size
        col_header = 0
        for i in range(self.N):
            display_string += str(col_header) + ' ' +' '*(space_size - len(str(col_header)))
            col_header += 1
        display_string += '\n'

        row_header = 0
        for row in self.display_grid:
            display_string += str(row_header) + ' ' +' '*(space_size - len(str(row_header)))
            col_header = 0
            for col in row:
                display_string += str(col) + ' '*(space_size)
                col_header += 1
            display_string += '\n'
            row_header += 1
        return display_string
