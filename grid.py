from typing import List
from figure import figure
from figures import get_random_figure


class grid:
    __figures: List[figure] = []

    def new_random_figure(self) -> figure:
        current_figure = get_random_figure()
        self.__figures.append(current_figure)
        return current_figure

    def delete_line(self):
        pass
