from ChessEnums import Space


class Coord:
    def __init__(self, c: int, r: int) -> None:
        self.c = c
        self.r = r

    @classmethod
    def fromSpace(cls, par_space: Space):
        c = par_space // 8
        r = par_space % 8
        return cls(c, r)

    def isValid(self):
        is_valid = (0 <= self.c < 8) and (0 <= self.r < 8)
        return is_valid

    def toSpace(self) -> Space:
        return Space(8*self.c + self.r)
