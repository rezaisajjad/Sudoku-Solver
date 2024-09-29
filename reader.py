
class Reader(object):
    """
    docstring
    """
    def __init__(self, path) -> None:
        self._path = path
        self._file = open(path,'rt')
        self._data = []
        self.read_sudoku()

    def read_sudoku(self):
        """
        docstring
        """
        for i in self._file.readlines():
            self._data.append([int(i) for i in i.split()])
    
    @property
    def sudoku(self):
        return self._data