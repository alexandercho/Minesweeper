from Game import *
import random
import numpy as np
class Solver:
    def __init__(self):
        N = 10
        M = 10
        win_count = 0
        for i in range(100000):
            game = Game(N, M)
            self.solve(game)
            if game.is_win():
                win_count += 1
        self._win_rate = win_count/100000
        print(win_count/100000)

    def solve(self, game):
        #corner is safest but middle cells will reveal more information
        #first move should always be a corner because it has the highest
        #Fixed corner has a 90% chance of working. Random corner works the same with higher variance
        first_move = (0,0)
        game.play_move(0,0)
        while not game.game_over:
            row, col = self.get_next_move(game)
            game.play_move(row, col)

    def get_next_move(self, game):
        #return random.choice(game.remaining_cells)
        cell_to_index = dict((i,j) for i,j in zip(game.remaining_cells, [k for k in range(len(game.remaining_cells))]))
        index_to_cell = dict((cell_to_index[key],key) for key in cell_to_index)



        numbers = game.get_numbers()
        A = [[0 for i in range(len(game.remaining_cells))] for j in range(len(numbers))]
        y = []

        for i in range(len(numbers)):
            for j in range(-1,2):
                for k in range(-1,2):
                    adj_row, adj_col = numbers[i][0] + j, numbers[i][1] + k
                    if (adj_row, adj_col) in game.remaining_cells and (abs(j) + abs(k) == 1):
                        A[i][cell_to_index[(adj_row, adj_col)]] = 1
            y += [numbers[i][2]]
        x = np.linalg.lstsq(A,y,rcond=1)[0].tolist()
        return index_to_cell[x.index(min(x))]
        #print(x)
        return random.choice(game.remaining_cells)
        potential_moves = game.remaining_cells
        potential_moves = sorted(potential_moves, key=lambda x: game.neighbor_sum(x[0],x[1]), reverse=False)
        return potential_moves[0]


    def double_set_single_point(self, game):
        """opener = First-Move()
            S ← {opener}
            Q ← {}
            while game is not over do
                if S is empty then
                    x ← Select-Random-Square()
                    S ← {x}
                end if
                while S is not empty do
                    x ← S.remove()
                    probe(x)
                    if x = mine then
                        return failure
                    end if
                    if isAFN(x) = True then
                        S ← S ∪ Unmarked-Neighbors(x)
                    else
                        Q ← Q ∪ {x}
                    end if
                end while
                for q ∈ Q do
                    if isAMN(q) = True then
                        for y ∈ Unmarked-Neighbors(q) do
                            mark(y)
                        end for
                        Q.remove(q)
                    end if
                end for
                for q ∈ Q do
                    if isAFN(q) = True then
                        S ← S ∪ Unmarked-Neighbors(q)
                        Q.remove(q)
                    end if
                end for
            end while

            first_move = (0,0)
            S = set([first_move])
            Q = set()
            while not game.game_over:
                if not S:
                    x = get_random_square(game)
                    S = set([x])
                while S:
                    x = S.pop(0)
                    game.play_move(x[0], x[1])
                    if isAFN(x):
                        S = S + unmarked_neighbors(x)
                    else:
                        Q = Q + set(x)
                for q in Q:
                    if isAFN(q):
                        S = S + unmarked_neighbors(q)
                        Q.remove(q)
            return None"""
        return None

    def is_AFN(self,game): #All free neighbors
        return False

    def get_random_square(self, game):
        return (0,0)

if __name__ == '__main__':
    s = Solver()
