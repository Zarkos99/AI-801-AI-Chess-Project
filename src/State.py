
from chess_enums import Space
from chess_enums import Player
from chess_enums import Piece
import numpy


class Action:
    board: numpy.array  # of Piece, SpaceCount
    king_space: numpy.array  # of Space, PlayerCount
    king_moved: numpy.array  # of bool, PlayerCount
    rookA_moved: numpy.array  # of bool, PlayerCount
    rookH_moved: numpy.array  # of bool, PlayerCount
    moves: list  # of Actions
    player: Player
    check: bool

    def __init__(self) -> None:
        board = {Space.___}
        board[Space.A2] = board[Space.B2] = board[Space.C2] = board[Space.D2] = board[
            Space.E2] = board[Space.F2] = board[Space.G2] = board[Space.H2] = Piece.W_P
        board[Space.B1] = board[Space.G1] = Piece.W_N
        board[Space.C1] = board[Space.F1] = Piece.W_B
        board[Space.A1] = board[Space.H1] = Piece.W_R
        board[Space.D1] = Piece.W_Q
        board[Space.E1] = Piece.W_K

        board[Space.A7] = board[Space.B7] = board[Space.C7] = board[Space.D7] = board[
            Space.E7] = board[Space.F7] = board[Space.G7] = board[Space.H7] = Piece.B_P
        board[Space.B8] = board[Space.G8] = Piece.B_N
        board[Space.C8] = board[Space.F8] = Piece.B_B
        board[Space.A8] = board[Space.H8] = Piece.B_R
        board[Space.D8] = Piece.B_Q
        board[Space.E8] = Piece.B_K

        self.king_space = {Space.E1, Space.E8}
        self.king_moved = {False, False}
        self.rookA_moved = {False, False}
        self.rookH_moved = {False, False}
        self.player = Player(len(self.moves) % 2)
        self.check = False

    @classmethod
    def __eq__(self, par_state) -> bool:
        self.board = par_state.board
        self.moves = par_state.moves
        self.king_space = par_state.king_space
        self.king_moved = par_state.king_moved
        self.rookA_moved = par_state.rookA_moved
        self.rookH_moved = par_state.rookH_moved
        self.player = par_state.player
        self.check = False
        return self
