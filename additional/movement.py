
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