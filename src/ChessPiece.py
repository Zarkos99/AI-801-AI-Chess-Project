from ChessEnums import Piece_Type
from ChessEnums import Player


class ChessPiece:
    """Defines a UI Chess Piece"""

    def __init__(self, piece_type: Piece_Type = Piece_Type.___, color: Player = Player.___) -> None:
        self.piece_type = piece_type
        self.color = color

    def __repr__(self):
        return f"{self.color}{self.piece_type}"

    def __eq__(self, par_rhs) -> bool:
        return self.piece_type == par_rhs.piece_type and self.color == par_rhs.color
