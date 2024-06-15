from chess_enums import Space


class Coord:
    def __init__(self, c: int, r: int) -> None:
        self.c = c
        self.r = r

    @classmethod
    def fromSpace(cls, par_space: Space) -> None:
        c = par_space / 8
        r = par_space % 8
        return cls(c, r)

    def toSpace(self) -> Space:
        return Space(8*self.c + self.r)
