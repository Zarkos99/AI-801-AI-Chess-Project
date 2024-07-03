from ChessEnums import Space
from ChessEnums import Piece_Type


class Action:
    orig: Space
    dest: Space
    promotion: Piece_Type

    # Default parameters of initialization function are equivalent to Checkmate Action
    def __init__(self, par_orig: Space = Space.A1, par_dest: Space = Space.A1, par_promotion: Piece_Type = Piece_Type.___) -> None:
        self.orig = par_orig
        self.dest = par_dest
        self.promotion = par_promotion

    def __eq__(self, par_rhs) -> bool:
        return self.orig == par_rhs.orig and self.dest == par_rhs.dest and self.promotion == par_rhs.promotion
