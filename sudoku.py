
class Solver(object):
    """
    docstring
    """

    def __init__(self,sudoku) -> None:
        self._sudoku = sudoku
        self._result = None
        self._init_game()

    def _init_game(self):
        for i in range(9):
            for j in range(9):
                _value = self._sudoku[i][j]
                if _value == 0:
                    self._sudoku[i][j] = [x for x in range(1,10)]

    def _calculate_square(self,i,j):
        return 3*(j//3) + (i//3)

    def _check_back_track(self) -> bool:
        _rows = [[] for i in range(9)]
        _columns = [[] for i in range(9)]
        _squares = [[] for i in range(9)]
        for i in range(9):
            for j in range(9):
                _value = self._sudoku[i][j]
                _square = self._calculate_square(i,j)
                if isinstance(_value,list):
                    continue
                if _value in _rows[i] or _value in _columns[j] or _value in _squares[_square]:
                    return True
                _rows[i].append(_value)
                _columns[j].append(_value)
                _squares[_square].append(_value)
        return False

    def _is_solved(self):
        for i in range(9):
            for j in range(9):
                if isinstance(self._sudoku[i][j],list):
                    return False
        return not self._check_back_track()

    def _back_track_sovle(self) -> bool:
        if self._check_back_track():
            return False
        if self._is_solved():
            return True

        for i in range(9):
            for j in range(9):
                _value = self._sudoku[i][j]
                if isinstance(_value,list):
                    for k in _value:
                        self._sudoku[i][j] = k
                        if self._back_track_sovle():
                            return True
                        self._sudoku[i][j] = [x for x in range(1,10)]
                    return False

    @property
    def result(self):
        if not self._is_solved():
            self._result = self._back_track_sovle()
            if self._result == False:
                raise Exception('Not valid game')
        return self.SudoList(self._sudoku)
    
    class SudoList(object):
        def __init__(self,data):
            self.data = data
        def __str__(self):
            _str = []
            for i in range(9):
                if i%3 == 0 and i!= 0:
                    _str.extend(['-' for _ in range(23)])
                    _str.append('\n')
                for j in range(9):
                    if j%3 == 0 and j!= 0:
                        _str.append(' | ')
                    _str.append(f'{self.data[i][j]} ')
                _str.append('\n')
            return ''.join(_str)