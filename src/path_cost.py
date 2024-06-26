"""module for calculating path cost"""
import numpy as np
from chess_enums import Piece
from chess_enums import Player
from state import State

class PathCost:
    """helps calculate the 'cost' of a path"""
    def __init__(self, par_state: State) -> None:
        player = par_state.player

        # We intend to divide by 0 sometimes, and we want this to result in 'inf'.
        # Numpy types allow this, default Python types throw an exception.
        w_pieces = np.int32(0)
        b_pieces = np.int32(0)

        for piece in par_state.board:
            match piece:
                case Piece.W_P:
                    w_pieces += 1
                    break
                case Piece.W_N:
                    w_pieces += 2
                    break
                case Piece.W_B:
                    w_pieces += 3
                    break
                case Piece.W_R:
                    w_pieces += 5
                    break
                case Piece.W_Q:
                    w_pieces += 9
                    break
                case Piece.B_P:
                    b_pieces += 1
                    break
                case Piece.B_N:
                    b_pieces += 2
                    break
                case Piece.B_B:
                    b_pieces += 3
                    break
                case Piece.B_R:
                    b_pieces += 5
                    break
                case Piece.B_Q:
                    b_pieces += 9
                    break
                case _:
                    break

        self.piece_weight = (
            w_pieces / b_pieces) if player == Player.White else (b_pieces / w_pieces)
        self.child_count = 0
        self.min_child_cost = 0.0
        self.expanded = False

    def __float__(self) -> float:
        if not self.expanded:
            return self.piece_weight
        if self.child_count == 0:
            return 0
        return 1.0 / self.min_child_cost
