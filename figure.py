from abc import ABC, abstractmethod
from typing import Tuple, List
from additional.movement import coords, moving_side


class cell:
    __number: int
    __coords: coords = coords(0, 0)
    __created: bool = False

    def get_number(self) -> int:
        return self.__number

    def is_created(self) -> bool:
        return self.__created

    def set_number(self, number: int):
        if not self.__created:
            self.__number = number
            self.__created = True

    def __init__(self, x: int, y: int):
        self.__coords = coords(x, y)

    def move(self, move_X: int, move_Y: int):
        self.__coords.x += move_X
        self.__coords.y += move_Y

    def move(self, move: coords):
        self.__coords.x += move.x
        self.__coords.y += move.y

    def get_coords(self) -> coords:
        return self.__coords

    def get_x(self) -> int:
        return self.__coords.x

    def get_y(self) -> int:
        return self.__coords.y


class figure(ABC):
    __main_cell_x: int = 2
    __main_cell_y: int = 2
    __color: str

    __cell_coords: List[List[List[int]]]
    __cells: List[cell] = []
    __main_cell: cell
    __state: int = 0

    def __init__(self) -> None:
        self.__cells = []
        self.__do_with_cell_coords(self.__create_cells)

    # this is an auxiliary variable, needed to move all cells by "rotate" method
    __cell_parse_index: int

    def rotate(self, state: int) -> None:
        self.__state = (self.__state + 1) // len(self.__cell_coords)
        self.__cell_parse_index = 0
        self.__do_with_cell_coords(self.__move_cells_for_rotate)

    def fall(self) -> None:
        self.move(moving_side.DOWN)

    def move(self, side: coords) -> None:
        for _cell in self.get_cells_with_main():
            _cell.move(side)

    def get_cells(self) -> List[cell]:
        return self.__cells

    def get_cells_with_main(self) -> List[cell]:
        all_cells = list(self.__cells)
        all_cells.append(self.__main_cell)
        return all_cells

    def get_color(self) -> str:
        return self.__color

    def get_state_number(self) -> int:
        return self.__state

    def get_state(self, number: int):
        return self.__cell_coords[number]

    def __do_with_cell_coords(self, function):
        for row in range(len(self.__cell_coords[self.__state])):
            for column in range(len(self.__cell_coords[self.__state][row])):
                if self.__cell_coords[self.__state][row][column] == 1:
                    function(row, column)

    def __create_cells(self, row: int, column: int) -> None:
        if row == self.__main_cell_y and column == self.__main_cell_x:
            self.__main_cell = cell(column, row)
        else:
            self.__cells.append(cell(column, row))

    def __move_cells_for_rotate(self, row: int, column: int):
        if self.__cell_coords[row][column] == 1:
            if not (row == self.__main_cell_y and column == self.__main_cell_x):
                self.__cells[self.__cell_parse_index].move(
                    self.__main_cell.get_x() + column - self.__main_cell_x,
                    self.__main_cell.get_y() + row - self.__main_cell_y)
                self.__cell_parse_index += 1

    def cell_coords(self):
        return self.__cell_coords
