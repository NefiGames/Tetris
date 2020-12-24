from typing import List
from figure import figure
from figures import get_random_figure
from additional.movement import coords


class grid:
    width: int = 5
    height: int = 10

    __figures: List[figure] = []
    __falling_figure: figure

    def new_random_figure(self) -> figure:
        self.__falling_figure = get_random_figure()
        return self.__falling_figure

    def delete_line(self, y: int) -> None:
        for _figure in self.__figures:
            for _cell in _figure.get_cells():
                if _cell.get_y() == y:
                    del _cell

    def figure_falled(self) -> bool:
        for _cell in self.__falling_figure:
            if not self.is_cell_free(_cell.get_x, _cell.get_y + 1):
                return True
        return False

    def is_cell_free(self, x: int, y: int) -> bool:
        for _figure in self.__figures:
            for _cell in _figure.get_cells():
                if _cell.get_y() == y and _cell.get_x() == x:
                    return False
        return True

    def try_fall(self):
        if not self.figure_falled():
            self.__falling_figure.fall()
        else:
            self.__figures.append(self.__falling_figure)
            self.new_random_figure()
