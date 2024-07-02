from ChessEnums import Space
from ChessEnums import Piece_Type


class Action:
    orig: Space
    dest: Space
    promotion: Piece_Type

    # Default parameters of initialization function are equivalent to Checkmate Action
    def __init__(self, par_orig: Space = Space.A1, par_dest: Space = Space.A1, par_promotion: Piece_Type = Piece_Type.___) -> None:
        if par_orig is None or not isinstance(par_orig, Space):
            raise ValueError("Invalid origin")
        if par_dest is None or not isinstance(par_dest, Space):
            raise ValueError("Invalid destination")
        if par_promotion is None or not isinstance(par_promotion, Piece_Type):
            raise ValueError("Invalid promotion")

        self.orig = par_orig
        self.dest = par_dest
        self.promotion = par_promotion

    def __eq__(self, par_rhs) -> bool:
        if not isinstance(par_rhs, Action):
            return False
        return self.orig == par_rhs.orig and self.dest == par_rhs.dest and self.promotion == par_rhs.promotion
