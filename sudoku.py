
class Solver(object):
    """
    docstring
    """

    def __init__(self,sudoku) -> None:
        self._sudoku = sudoku
        self._is_solved = False
        self._result = None

    def __sovle__(parameter_list):
        """
        docstring
        """
        print("solving")

    @property
    def result(self):
        if not self._is_solved:
            self.__sovle__()
        return self._result