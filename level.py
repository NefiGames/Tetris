class results:
    __prize_for_lines = [50, 200, 400, 700]
    __level: int = 1
    __score: int = 0

    def __init__(self):
        pass

    def add_score_for_lines(self, deleted_lines_count: int):
        if deleted_lines_count > 4:
            assert "There can be 4 lines maximum"
        else:
            self.__score += self.__prize_for_lines[deleted_lines_count - 1]
            self.__check_level()

    def add_score_for_speed(self):
        self.__score += 1
        self.__check_level()

    def __check_level(self):
        if 2 ** (self.__level + 9) < self.__score:
            self.__level += 1

    def get_level(self):
        return self.__level

    def get_score(self):
        return self.__score
