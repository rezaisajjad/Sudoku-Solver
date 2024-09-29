from reader import Reader
from sudoku import Solver


reader = Reader('s1.txt')
sudoku = Solver(reader.sudoku)

print(sudoku.result)