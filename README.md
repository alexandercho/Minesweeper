# Minesweeper

## Playing the game  
Run PlayGame.py with Python 3 in your terminal

## Running the solver
Run Solver.py with Python 3 in your terminal. (This took me about 7 min)

## Solver Strategy
The solver consists of two parts. The first part will always play a corner move  
first because corner moves mathematically have the highest expected number of
uncovered cells. After, the solver uses a least squares solution to find the  
cell with the least likely possibility of being a mine. Given that the test runs
on 100,000 samples of 10x10 squares with 10 mines, the highest average expected
win count should be 90,000 given that for any strategy, the probability of losing
in the first move is 10%. The solver does marginally better than random choices
when run under these conditions but the gap between that and randomly solving
increases as the mine rate of the board increases. For example, the win rate is
50% higher with this strategy than randomly selecting cells when there are 40
mines in a 10x10 board.
