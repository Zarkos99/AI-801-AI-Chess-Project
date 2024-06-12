import chess_enums


class Action:
    orig: chess_enums.Space
    dest: chess_enums.Space
    promotion: chess_enums.Piece

    # Default parameters of initialization function are equivalent to Checkmate Action
    def __init__(self, par_orig: chess_enums.Space = chess_enums.Space.A1, par_dest: chess_enums.Space = chess_enums.Space.A1, par_promotion: chess_enums.Piece = chess_enums.Piece.___) -> None:
        self.orig = par_orig
        self.dest = par_dest
        self.promotion = par_promotion

    @classmethod
    def __eq__(self, par_rhs) -> bool:
        return self.orig == par_rhs.orig and self.dest == par_rhs.dest and self.promotion == par_rhs.promotion
