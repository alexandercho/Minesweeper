from Game import *

class Solver:
    def __init__(self):
        N = 10
        M = 10
        win_count = 0
        for i in range(100):
            game = Game(N, M)
            self.solve(game)
            if game.is_win():
                win_count += 1

    def solve(self, game):
        #corner is safest but middle cells will reveal more information
        #first move should always be a corner because it has the highest
        #Fixed corner has a 90% chance of working. Random corner works the same with higher variance
        while not game.game_won:
            row, col = self.get_next_move(game.get_display())
            game.play_move(row, col)

    def get_next_move(self, game):
        row, col = 0,0
        gs = GameState(game.get_display())
        return row, col

class GameState:

    def __init__(self, display):
        N = len(display)
        for row in range()
            self.prob = [[0 for i in range(N)] 0 for i in range(N)]



if __name__ == '__main__':
    s = Solver()
