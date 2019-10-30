from GameBoard import *
from Game import *

def test_get_uncovered_cells():
    sizes = [5, 10, 20, 30]
    M = 2

    for N in sizes:
        g = GameBoard(N,M)
        i, j = 0, 0

        while g.is_mine(i, j):
            i += 1
            if g.is_mine(i, j):
                j += 1

        num_uncovered = len(g.get_uncovered_cells(i,j))

        print('Given a size ' + str(N) + ' board, the first move uncovers '+ str(num_uncovered) + ' cells.')
        print('There should be ' + str(M) + ' mines.')
        print('There are ' + str(N**2-num_uncovered) + ' mines left.')

def test_play_move():
    sizes = [3,4,5]
    M = 2

    for N in sizes:
        g = Game(N,M)
        i, j = 0, 0
        print(str(g.displayboard))

        while g.gameboard.is_mine(i, j):
            i += 1
            if g.gameboard.is_mine(i, j):
                j += 1
        g.play_move(i,j)
        print(str(g.displayboard))

def test_display():
    g = Game(101,2)
    i, j = 0, 0
    print(str(g.displayboard))

if __name__ == '__main__':
    test_display()
