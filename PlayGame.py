from GameBoard import *
class Game:
    def __init__(self, N, M):
        self.size = N
        self.num_mines = M
        self.board = GameBoard(N,M)

        self.num_uncovered = 0

    def is_win():
        return N**2 - M == self.num_uncovered

    def is_loss(row, col):
        return self.board.is_mine(row,col)

if __name__ == '__main__':
    print('What is the length of your square grid?')
    N = input()
    while (type(N) is not int()):
        try:
            N = int(N)
            break
        except ValueError:
            print('Please enter an integer value')
            N = input()

    print('How many mines are in your grid?')
    M = input()
    while (type(M) is not int()):
        try:
            M = int(M)
            break
        except ValueError:
            print('Please enter an integer value')
            M = input()

    b = Board(N,M)

    print('How many mines are in your grid?')
    M = input()
    while (type(M) is not int()):
        try:
            M = int(M)
            break
        except ValueError:
            print('Please enter an integer value')
            M = input()

    for row in b.grid:
        print(row)
