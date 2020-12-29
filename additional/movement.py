
class coords:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class moving_side:
    STAY = coords(0, 0)
    RIGHT = coords(1, 0)
    LEFT = coords(-1, 0)
    UP = coords(0, -1)
    DOWN = coords(0, 1)
    DOUBLE_LEFT = coords(-2, 0)
    DOUBLE_RIGHT = coords(2, 0)
    DOUBLE_DOWN = coords(0, 2)
    DOUBLE_UP = coords(0, -2)
    all_moves = [RIGHT, LEFT, UP, DOWN, DOUBLE_RIGHT, DOUBLE_LEFT, DOUBLE_UP, DOUBLE_DOWN]