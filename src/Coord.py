import chess_enums


class Action:
    c: int
    r: int

    def __init__(self, par_space: chess_enums.Space) -> None:
        self.c = par_space / 8
        self.r = par_space % 8

    def __init__(self, par_c: int, par_r: int) -> None:
        self.c = par_c
        self.r = par_r

    @classmethod
    def __call__(self) -> chess_enums.Space:
        return chess_enums.Space(8*self.c + self.r)
