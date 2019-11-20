from Game import *
import random
import numpy as np
import time

class Solver:
    def __init__(self):
        N = 10
        M = 10

        self.win_count = 0
        for i in range(100000):
            game = Game(N, M)
            self.solve(game)
            if game.is_win():
                self.win_count += 1




    def solve_random(self, game):
        while not game.is_over():
            game.play_move(self.get_random_move(game))

    def solve(self, game):
        first_move = (0,0)
        game.play_move(first_move)
        while not game.is_over():
            game.play_move(self.get_next_move(game))

    def get_next_move(self, game):
        uncovered_nums = game.uncovered_numbers()
        cell_to_index = dict((cell, ind) for cell,ind in zip(game.remaining_cells, range(len(game.remaining_cells))))
        index_to_cell = dict((cell_to_index[key], key) for key in cell_to_index)


        A = [[0 for i in range(len(game.remaining_cells))] for j in range(len(uncovered_nums))]
        y = []

        for i in range(len(uncovered_nums)):
            cell = (uncovered_nums[i][0], uncovered_nums[i][1])
            for adj_cell in game.get_adj_cells(cell):
                if adj_cell in game.remaining_cells:
                        A[i][cell_to_index[adj_cell]] = 1
            y += [uncovered_nums[i][2]]
        x = np.linalg.lstsq(A,y,rcond=1)[0].tolist()

        no_adj_nums = [cell for cell in game.remaining_cells if not game.is_adj_to_num(cell)]
        if no_adj_nums:
            prob_mine = (game.M - min(sum([1 for i in x if i > 0.5]),game.M-1))/len(no_adj_nums)
            for cell in no_adj_nums:
                x[cell_to_index[cell]] = prob_mine
        return index_to_cell[x.index(min(x))]

    def get_random_move(self, game):
        return random.choice(game.remaining_cells)

if __name__ == '__main__':
    t = time.process_time()
    s = Solver()
    elapsed_time = time.process_time() - t
    print('The number of puzzles successfully solved out of 100,000 attempts is: ' + str(s.win_count))
    print('The total time to complete the 100,000 attempts is: ' + str(elapsed_time) + ' sec')
