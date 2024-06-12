import chess_enums
import numpy


class Action:
    board: numpy.array  # of Piece, SpaceCount
    king_space: numpy.array  # of Space, PlayerCount
    king_moved: numpy.array  # of bool, PlayerCount
    rookA_moved: numpy.array  # of bool, PlayerCount
    rookH_moved: numpy.array  # of bool, PlayerCount
    moves: list  # of Actions
    player: chess_enums.Player
    check: bool

    def __init__(self) -> None:
        board = {chess_enums.Space.___}
        board[chess_enums.Space.A2] = board[chess_enums.Space.B2] = board[chess_enums.Space.C2] = board[chess_enums.Space.D2] = board[
            chess_enums.Space.E2] = board[chess_enums.Space.F2] = board[chess_enums.Space.G2] = board[chess_enums.Space.H2] = chess_enums.Piece.W_P
        board[chess_enums.Space.B1] = board[chess_enums.Space.G1] = chess_enums.Piece.W_N
        board[chess_enums.Space.C1] = board[chess_enums.Space.F1] = chess_enums.Piece.W_B
        board[chess_enums.Space.A1] = board[chess_enums.Space.H1] = chess_enums.Piece.W_R
        board[chess_enums.Space.D1] = chess_enums.Piece.W_Q
        board[chess_enums.Space.E1] = chess_enums.Piece.W_K

        board[chess_enums.Space.A7] = board[chess_enums.Space.B7] = board[chess_enums.Space.C7] = board[chess_enums.Space.D7] = board[
            chess_enums.Space.E7] = board[chess_enums.Space.F7] = board[chess_enums.Space.G7] = board[chess_enums.Space.H7] = chess_enums.Piece.B_P
        board[chess_enums.Space.B8] = board[chess_enums.Space.G8] = chess_enums.Piece.B_N
        board[chess_enums.Space.C8] = board[chess_enums.Space.F8] = chess_enums.Piece.B_B
        board[chess_enums.Space.A8] = board[chess_enums.Space.H8] = chess_enums.Piece.B_R
        board[chess_enums.Space.D8] = chess_enums.Piece.B_Q
        board[chess_enums.Space.E8] = chess_enums.Piece.B_K

        self.king_space = {chess_enums.Space.E1, chess_enums.Space.E8}
        self.king_moved = {False, False}
        self.rookA_moved = {False, False}
        self.rookH_moved = {False, False}
        self.player = chess_enums.Player(len(self.moves) % 2)
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
