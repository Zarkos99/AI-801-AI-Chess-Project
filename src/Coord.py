"""A coord in the game space"""
from chess_enums import Space

class Coord:
    """Represents a space on the board"""
    def __init__(self, c: int, r: int) -> None:
        self.c = c
        self.r = r

    @classmethod
    def from_space(cls, par_space: Space):
        """distance from a spce"""
        c = par_space // 8
        r = par_space % 8
        return cls(c, r)

    def is_valid(self):
        """is the coord within the board"""
        is_valid = (0 <= self.c < 8) and (0 <= self.r < 8)
        return is_valid

    def to_space(self) -> Space:
        """distance to space"""
        return Space(8*self.c + self.r)
