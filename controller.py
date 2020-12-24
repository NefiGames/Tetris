from grid import grid
from visual import visual
from level import results
from additional.movement import moving_side, coords


class controller:
    __grid: grid
    __results: results
    delay = 500

    def __init__(self):
        assert "Controller can not be created. It is a static class"

    @staticmethod
    def grid() -> grid:
        return controller.__grid

    @staticmethod
    def results() -> results:
        return controller.__results

    @staticmethod
    def initialize_window():
        controller.__initialize_menu()
        visual.window().initialize()

    @staticmethod
    def __initialize_menu():
        visual.menu().initialize(start_button_callback=controller.initialize_game)

    @staticmethod
    def initialize_game():
        visual.game().initialize()
        controller.__grid = grid()
        controller.bind_keys()
        controller.fall_figure()

    @staticmethod
    def bind_keys():
        visual.game().canvas().bind('<Left>', lambda event: controller.left_right_move(moving_side.LEFT))
        visual.game().canvas().bind('<Right>', lambda event: controller.left_right_move(moving_side.RIGHT))
        visual.game().canvas().focus_set()

    @staticmethod
    def fall_figure():
        controller.grid().try_figure_fall()
        visual.game().refresh_figures()
        visual.window().root().after(controller.delay, lambda: controller.fall_figure())

    @staticmethod
    def left_right_move(side: coords):
        controller.grid().try_move_figure(side)
        visual.game().refresh_figures()
