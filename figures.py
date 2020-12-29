from figure import figure
from random import randint
from additional.colors import colors


class figure_T(figure):
    _figure__color = colors.figure_T
    _figure__cell_coords = [[[0, 0, 0, 0, 0],
                             [0, 0, 1, 0, 0],
                             [0, 1, 1, 1, 0],
                             [0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0]],

                            [[0, 0, 0, 0, 0],
                             [0, 0, 1, 0, 0],
                             [0, 0, 1, 1, 0],
                             [0, 0, 1, 0, 0],
                             [0, 0, 0, 0, 0]],

                            [[0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0],
                             [0, 1, 1, 1, 0],
                             [0, 0, 1, 0, 0],
                             [0, 0, 0, 0, 0]],

                            [[0, 0, 0, 0, 0],
                             [0, 0, 1, 0, 0],
                             [0, 1, 1, 0, 0],
                             [0, 0, 1, 0, 0],
                             [0, 0, 0, 0, 0]]]


class figure_J(figure):
    _figure__color = colors.figure_J
    _figure__cell_coords = [[[0, 0, 0, 0, 0],
                             [0, 0, 1, 0, 0],
                             [0, 0, 1, 0, 0],
                             [0, 1, 1, 0, 0],
                             [0, 0, 0, 0, 0]],

                            [[0, 0, 0, 0, 0],
                             [0, 1, 0, 0, 0],
                             [0, 1, 1, 1, 0],
                             [0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0]],

                            [[0, 0, 0, 0, 0],
                             [0, 0, 1, 1, 0],
                             [0, 0, 1, 0, 0],
                             [0, 0, 1, 0, 0],
                             [0, 0, 0, 0, 0]],

                            [[0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0],
                             [0, 1, 1, 1, 0],
                             [0, 0, 0, 1, 0],
                             [0, 0, 0, 0, 0]]]


class figure_Z(figure):
    _figure__color = colors.figure_Z
    _figure__cell_coords = [[[0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0],
                             [0, 1, 1, 0, 0],
                             [0, 0, 1, 1, 0],
                             [0, 0, 0, 0, 0]],

                            [[0, 0, 0, 0, 0],
                             [0, 0, 0, 1, 0],
                             [0, 0, 1, 1, 0],
                             [0, 0, 1, 0, 0],
                             [0, 0, 0, 0, 0]]]


class figure_O(figure):
    _figure__color = colors.figure_O
    _figure__cell_coords = [[[0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0],
                             [0, 1, 1, 0, 0],
                             [0, 1, 1, 0, 0],
                             [0, 0, 0, 0, 0]]]


class figure_S(figure):
    _figure__color = colors.figure_S
    _figure__cell_coords = [[[0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0],
                             [0, 0, 1, 1, 0],
                             [0, 1, 1, 0, 0],
                             [0, 0, 0, 0, 0]],

                            [[0, 0, 0, 0, 0],
                             [0, 0, 1, 0, 0],
                             [0, 0, 1, 1, 0],
                             [0, 0, 0, 1, 0],
                             [0, 0, 0, 0, 0]]]


class figure_L(figure):
    _figure__color = colors.figure_L
    _figure__cell_coords = [[[0, 0, 0, 0, 0],
                             [0, 0, 1, 0, 0],
                             [0, 0, 1, 0, 0],
                             [0, 0, 1, 1, 0],
                             [0, 0, 0, 0, 0]],

                            [[0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0],
                             [0, 1, 1, 1, 0],
                             [0, 1, 0, 0, 0],
                             [0, 0, 0, 0, 0]],

                            [[0, 0, 0, 0, 0],
                             [0, 1, 1, 0, 0],
                             [0, 0, 1, 0, 0],
                             [0, 0, 1, 0, 0],
                             [0, 0, 0, 0, 0]],

                            [[0, 0, 0, 0, 0],
                             [0, 0, 0, 1, 0],
                             [0, 1, 1, 1, 0],
                             [0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0]]]


class figure_I(figure):
    _figure__color = colors.figure_I
    _figure__cell_coords = [[[0, 0, 1, 0, 0],
                             [0, 0, 1, 0, 0],
                             [0, 0, 1, 0, 0],
                             [0, 0, 1, 0, 0],
                             [0, 0, 0, 0, 0]],

                            [[0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0],
                             [1, 1, 1, 1, 0],
                             [0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0]]]


all_figures = [figure_T, figure_J, figure_Z, figure_O, figure_S, figure_L, figure_I]


def get_random_figure():
    return all_figures[randint(0, len(all_figures)-1)]
