
from ChessEnums import Space, Piece_Type, Player
from ChessPiece import ChessPiece


class State:
    def __init__(self) -> None:
        # regular flat array
        self.board = [ChessPiece()]*len(Space)
        self.board[Space.A2] = self.board[Space.B2] = self.board[Space.C2] = self.board[Space.D2] = self.board[
            Space.E2] = self.board[Space.F2] = self.board[Space.G2] = self.board[Space.H2] = ChessPiece(Piece_Type.PAWN, Player.WHITE)
        self.board[Space.B1] = self.board[Space.G1] = ChessPiece(
            Piece_Type.KNIGHT, Player.WHITE)
        self.board[Space.C1] = self.board[Space.F1] = ChessPiece(
            Piece_Type.BISHOP, Player.WHITE)
        self.board[Space.A1] = self.board[Space.H1] = ChessPiece(
            Piece_Type.ROOK, Player.WHITE)
        self.board[Space.D1] = ChessPiece(Piece_Type.QUEEN, Player.WHITE)
        self.board[Space.E1] = ChessPiece(Piece_Type.KING, Player.WHITE)

        self.board[Space.A7] = self.board[Space.B7] = self.board[Space.C7] = self.board[Space.D7] = self.board[
            Space.E7] = self.board[Space.F7] = self.board[Space.G7] = self.board[Space.H7] = ChessPiece(Piece_Type.PAWN, Player.BLACK)
        self.board[Space.B8] = self.board[Space.G8] = ChessPiece(
            Piece_Type.KNIGHT, Player.BLACK)
        self.board[Space.C8] = self.board[Space.F8] = ChessPiece(
            Piece_Type.BISHOP, Player.BLACK)
        self.board[Space.A8] = self.board[Space.H8] = ChessPiece(
            Piece_Type.ROOK, Player.BLACK)
        self.board[Space.D8] = ChessPiece(Piece_Type.QUEEN, Player.BLACK)
        self.board[Space.E8] = ChessPiece(Piece_Type.KING, Player.BLACK)

        self.moves = []
        self.king_space = [Space.E1, Space.E8]
        self.king_moved = [False, False]
        self.rookA_moved = [False, False]
        self.rookH_moved = [False, False]
        self.player = Player.WHITE if len(self.moves) % 2 == 0 else Player.BLACK
        self.check = False
