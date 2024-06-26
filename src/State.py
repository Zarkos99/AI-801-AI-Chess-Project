"""state"""
from chess_enums import Space
from chess_enums import Player
from chess_enums import Piece

class State:
    """App State"""
    def __init__(self) -> None:
        self.board = [Piece.___]*len(Space)
        self.board[Space.A2] = self.board[Space.B2] = self.board[Space.C2] = self.board[
            Space.D2] = self.board[Space.E2] = self.board[Space.F2] = self.board[
            Space.G2] = self.board[Space.H2] = Piece.W_P
        self.board[Space.B1] = self.board[Space.G1] = Piece.W_N
        self.board[Space.C1] = self.board[Space.F1] = Piece.W_B
        self.board[Space.A1] = self.board[Space.H1] = Piece.W_R
        self.board[Space.D1] = Piece.W_Q
        self.board[Space.E1] = Piece.W_K

        self.board[Space.A7] = self.board[Space.B7] = self.board[Space.C7] = self.board[
            Space.D7] = self.board[Space.E7] = self.board[Space.F7] = self.board[
            Space.G7] = self.board[Space.H7] = Piece.B_P
        self.board[Space.B8] = self.board[Space.G8] = Piece.B_N
        self.board[Space.C8] = self.board[Space.F8] = Piece.B_B
        self.board[Space.A8] = self.board[Space.H8] = Piece.B_R
        self.board[Space.D8] = Piece.B_Q
        self.board[Space.E8] = Piece.B_K

        self.moves = []
        self.king_space = [ Space.E1, Space.E8 ]
        self.king_moved = [ False, False ]
        self.rook_a_moved = [ False, False ]
        self.rook_h_moved = [ False, False ]
        self.player = Player(len(self.moves) % 2)
        self.check = False
