from chess_enums import Space

class Coord:
    c: int
    r: int

    def __init__(self, par_c: int, par_r: int) -> None:
        self.c = par_c
        self.r = par_r

    @classmethod
    def fromSpace(cls, par_space: Space) -> None:
        c = par_space / 8
        r = par_space % 8
        cls(c, r)

    @classmethod
    def __call__(self) -> Space:
        return Space(8*self.c + self.r)
