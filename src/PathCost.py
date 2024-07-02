from ChessEnums import Player, Piece_Type
import State
import numpy as np


class PathCost:

    def __init__(self, par_state: State) -> None:
        player = par_state.player

        # We intend to divide by 0 sometimes, and we want this to result in 'inf'.
        # Numpy types allow this, default Python types throw an exception.
        w_pieces = np.int32(0)
        b_pieces = np.int32(0)

        for chess_piece in par_state.board:
            cost = 0
            match chess_piece.piece_type:
                case Piece_Type.PAWN:
                    cost = 1
                case Piece_Type.KNIGHT:
                    cost = 2
                case Piece_Type.BISHOP:
                    cost = 3
                case Piece_Type.ROOK:
                    cost = 5
                case Piece_Type.QUEEN:
                    cost = 9

            if (chess_piece.player == Player.WHITE):
                w_pieces += cost
            else:
                b_pieces += cost

        self.piece_weight = (
            w_pieces / b_pieces) if player == Player.WHITE else (b_pieces / w_pieces)
        self.child_count = 0
        self.min_child_cost = 0.0
        self.expanded = False

    def __float__(self) -> float:
        if not self.expanded:
            return self.piece_weight
        if self.child_count == 0:
            return 0.0
        return 1.0 / self.min_child_cost
