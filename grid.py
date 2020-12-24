from typing import List
from figure import figure
from figures import get_random_figure, figure_Z
from additional.movement import coords, moving_side


class grid:
    __width: int = 10
    __height: int = 20

    __figures: List[figure] = []
    __falling_figure: figure

    def __init__(self):
        self.new_random_figure()

    def falling_figure(self) -> figure:
        return self.__falling_figure

    def new_random_figure(self) -> figure:
        self.__falling_figure = get_random_figure()()
        return self.__falling_figure

    def delete_line(self, y: int) -> None:
        for _figure in self.__figures:
            for _cell in _figure.get_cells_with_main():
                if _cell.get_y() == y:
                    del _cell
                elif _cell.get_y() < y:
                    _cell.move(moving_side.DOWN)

    def is_figure_falled(self) -> bool:
        for _cell in self.__falling_figure.get_cells_with_main():
            if not self.is_cell_free(_cell.get_x(), _cell.get_y() + 1):
                return True
        return False

    def is_cell_free(self, x: int, y: int) -> bool:
        if x < 0 or x >= self.__width:
            return False
        elif y < 0 or y >= self.__height:
            return False
        else:
            for _figure in self.__figures:
                for _cell in _figure.get_cells_with_main():
                    if _cell.get_y() == y and _cell.get_x() == x:
                        return False
            return True

    def try_move_figure(self, side: coords):
        for _cell in self.falling_figure().get_cells_with_main():
            if not self.is_cell_free(_cell.get_x() + side.x, _cell.get_y() + side.y):
                return False
        self.__falling_figure.move(side)

    def try_figure_fall(self):
        if not self.is_figure_falled():
            self.__falling_figure.fall()
        else:
            self.__figures.append(self.__falling_figure)
            self.new_random_figure()

    def get_figures_with_falling(self):
        all_figures = list(self.__figures)
        all_figures.append(self.__falling_figure)
        return all_figures
