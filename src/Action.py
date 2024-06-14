from chess_enums import Space
from chess_enums import Piece


class Action:
    orig: Space
    dest: Space
    promotion: Piece

    # Default parameters of initialization function are equivalent to Checkmate Action
    def __init__(self, par_orig: Space = Space.A1, par_dest: Space = Space.A1, par_promotion: Piece = Piece.___) -> None:
        self.orig = par_orig
        self.dest = par_dest
        self.promotion = par_promotion

    def __eq__(self, par_rhs) -> bool:
        return self.orig == par_rhs.orig and self.dest == par_rhs.dest and self.promotion == par_rhs.promotion
