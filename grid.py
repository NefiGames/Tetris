from typing import List
from figure import figure
from figures import get_random_figure, figure_Z
from additional.movement import coords, moving_side


class grid:
    __width: int = 10
    __height: int = 20

    __figures: List[figure] = []
    __falling_figure: figure
    __deleted_cells: List[int] = []

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
                    self.__deleted_cells.append(_cell.get_number())
                    _figure.delete_cell(_cell)
                elif _cell.get_y() < y:
                    _cell.move(moving_side.DOWN)

    def get_deleted_cells(self):
        a = self.__deleted_cells
        self.__deleted_cells = []
        return a

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
        return True

    def try_figure_fall(self):
        if not self.is_figure_falled():
            self.__falling_figure.fall()
        else:
            self.__figures.append(self.__falling_figure)
            self.check_lines_to_delete()
            self.new_random_figure()

    def check_lines_to_delete(self):
        lines = [0] * self.__height
        for _figure in self.__figures:
            for _cell in _figure.get_cells_with_main():
                lines[_cell.get_y()] += 1
        for i in range(len(lines)):
            if lines[i] == self.__width:
                self.delete_line(i)

    def try_figure_rotate(self):
        future_state_number = self.__falling_figure.get_state_number() + 1
        future_state = self.__falling_figure.get_state(future_state_number)
        main_cell = self.__falling_figure.get_main_cell().get_coords()

        for row in range(len(future_state)):
            for column in range(len(future_state[0])):
                if future_state[row][column] == 1:
                    if not self.is_cell_free(main_cell.x + column - 2, main_cell.y + row - 2):
                        if self.__try_remove_rotate_conflict():
                            self.try_figure_rotate()
                            return
                        else:
                            return None
        self.__falling_figure.rotate()

    def __try_remove_rotate_conflict(self):
        for side in moving_side.all_moves:
            if self.try_move_figure(side):
                return True
        return False

    def get_figures_with_falling(self):
        all_figures = list(self.__figures)
        all_figures.append(self.__falling_figure)
        return all_figures
