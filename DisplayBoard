import random

class GameBoard:
    def __init__(self, N, M):
        """
        The size of the grid to use (NxN square grid).
        The number of mines to be placed.
        """
        self.grid = [[0 for i in range(N)] for j in range(N)]


        #Samples or generates mines based on runtime
        if (M**2 * (2*N**2 - 1))/(2*N) < 1:
            mines = sample_mines(N,M)
        else:
            mines = generate_mines(N,M)

        for mine in mines:
            row, col = mine[0], mine[1]
            self.grid[row][col] = -1
            for i in range(-1,2):
                for j in range(-1,2):
                    adj_row = row + i
                    adj_col = col + j
                    if i != 0 or j != 0:
                        if (adj_row >= 0) and (adj_row < N) and (adj_col >= 0) and (adj_col < N):
                            if (adj_row, adj_col) not in mines:
                                self.grid[adj_row][adj_col] += 1
    def is_mine(self, row, col):
        return self.grid[row][col] == -1

#O(N*M)
def sample_mines(N,M):
    potential_mines = []
    for i in range(N):
        for j in range(M):
            potential_mines.append((i,j))
    return set(random.sample(potential_mines, M))

#O(2N^2 / (2*M*N^2 - M^2)
def generate_mines(N,M):
    mines = set()
    while len(mines) < M:
        mine = (random.randint(0, N-1), random.randint(0, N-1))
        mines.add(mine)
    return mines
