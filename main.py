from reader import Reader
from sudoku import Solver


reader = Reader('s1.txt')
sudoku = Solver(reader.sudoku)

f = open('result.txt','wt')
f.write(str(sudoku.result))
f.close()