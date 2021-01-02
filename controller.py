from grid import grid
from visual import visual
from level import results
from additional.movement import moving_side, coords
import keyboard


class controller:
    __grid: grid
    __results: results = results()
    __delay_falling = 500
    delay_moving = 70

    def __init__(self):
        assert "Controller can not be created. It is a static class"

    @staticmethod
    def grid() -> grid:
        return controller.__grid

    @staticmethod
    def get_normal_fall_delay():
        return int(500 // (1 + 0.2 * controller.__results.get_level()))

    @staticmethod
    def get_speed_fall_delay():
        return controller.get_normal_fall_delay() // 10

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
        visual.window().root().bind('<Up>', lambda event: controller.rotate_figure())
        controller.check_keys()
        controller.fall_figure()

    @staticmethod
    def check_keys():
        delay: int = controller.delay_moving
        if keyboard.is_pressed('Left'):
            controller.move(moving_side.LEFT)
        if keyboard.is_pressed('Right'):
            controller.move(moving_side.RIGHT)
        if keyboard.is_pressed('Down'):
            controller.move(moving_side.DOWN)
            controller.results().add_score_for_speed()
            delay = controller.get_speed_fall_delay()
        visual.window().root().after(delay, lambda: controller.check_keys())

    @staticmethod
    def rotate_figure():
        controller.grid().try_figure_rotate()
        visual.game().refresh_figures()

    @staticmethod
    def fall_figure():
        controller.__delay_falling = controller.get_normal_fall_delay()
        if not controller.grid().try_figure_fall():
            controller.loose_game()
            return
        deleted_lines = controller.grid().deleted_lines_count()
        if deleted_lines > 0:
            controller.results().add_score_for_lines(deleted_lines)
        visual.game().refresh_figures()
        visual.window().root().after(controller.__delay_falling, lambda: controller.fall_figure())

    @staticmethod
    def loose_game():  # TODO
        visual.game().remove_game()
        controller.__initialize_menu()
        controller.__grid = grid()

    @staticmethod
    def move(side: coords):
        controller.grid().try_move_figure(side)
        visual.game().refresh_figures()
