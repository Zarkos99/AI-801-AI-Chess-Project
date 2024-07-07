import unittest
from ChessPiece import ChessPiece
from ChessEnums import Piece_Type, Player, Space
from State import State
from Action import Action
from Coord import Coord
from Result import Result

class TestResultFunction(unittest.TestCase):

    def setUp(self):
        # Setting up initial board state as a 1D array
        self.initial_state = State()
        self.initial_state.board = [ChessPiece() for _ in range(64)]
        self.initial_state.board[Space.A1.value] = ChessPiece(Piece_Type.ROOK, Player.WHITE)
        self.initial_state.board[Space.E1.value] = ChessPiece(Piece_Type.KING, Player.WHITE)
        self.initial_state.board[Space.A8.value] = ChessPiece(Piece_Type.ROOK, Player.BLACK)
        self.initial_state.board[Space.E8.value] = ChessPiece(Piece_Type.KING, Player.BLACK)
        self.initial_state.board[Space.E2.value] = ChessPiece(Piece_Type.PAWN, Player.WHITE)
        self.initial_state.board[Space.E7.value] = ChessPiece(Piece_Type.PAWN, Player.BLACK)
        self.initial_state.board[Space.D4.value] = ChessPiece(Piece_Type.PAWN, Player.WHITE)

        self.initial_state.player = Player.WHITE
        self.initial_state.king_space = [Space.E1, Space.E8]
        self.initial_state.king_moved = [False, False]
        self.initial_state.rookA_moved = [False, False]
        self.initial_state.rookH_moved = [False, False]
        self.initial_state.moves = []

    def test_normal_move(self):
        action = Action(Space.E2, Space.E4)
        new_state = Result(self.initial_state, action)
        self.assertEqual(new_state.board[Space.E4.value], ChessPiece(Piece_Type.PAWN, Player.WHITE))
        self.assertEqual(new_state.board[Space.E2.value], ChessPiece())

    def test_capture(self):
        self.initial_state.board[Space.D5.value] = ChessPiece(Piece_Type.PAWN, Player.BLACK)
        action = Action(Space.D4, Space.D5)
        new_state = Result(self.initial_state, action)
        self.assertEqual(new_state.board[Space.D5.value], ChessPiece(Piece_Type.PAWN, Player.WHITE))
        self.assertEqual(new_state.board[Space.D4.value], ChessPiece())

    def test_en_passant(self):
        self.initial_state.board[Space.D5.value] = ChessPiece(Piece_Type.PAWN, Player.BLACK)
        action = Action(Space.E2, Space.E4)
        Result(self.initial_state, action)
        self.initial_state.player = Player.BLACK
        action = Action(Space.D5, Space.E6)
        new_state = Result(self.initial_state, action)
        self.assertEqual(new_state.board[Space.E6.value], ChessPiece(Piece_Type.PAWN, Player.BLACK))
        self.assertEqual(new_state.board[Space.E5.value], ChessPiece())

    def test_castling_kingside(self):
        action = Action(Space.E1, Space.G1)
        new_state = Result(self.initial_state, action)
        self.assertEqual(new_state.board[Space.G1.value], ChessPiece(Piece_Type.KING, Player.WHITE))
        self.assertEqual(new_state.board[Space.F1.value], ChessPiece(Piece_Type.ROOK, Player.WHITE))
        self.assertEqual(new_state.board[Space.E1.value], ChessPiece())
        self.assertEqual(new_state.board[Space.H1.value], ChessPiece())

    def test_promotion(self):
        action = Action(Space.E7, Space.E8, promotion=Piece_Type.QUEEN)
        new_state = Result(self.initial_state, action)
        self.assertEqual(new_state.board[Space.E8.value], ChessPiece(Piece_Type.QUEEN, Player.WHITE))

    def test_check(self):
        self.initial_state.board[Space.D4.value] = ChessPiece(Piece_Type.ROOK, Player.BLACK)
        action = Action(Space.D4, Space.E4)
        new_state = Result(self.initial_state, action)
        self.assertTrue(new_state.check)

if __name__ == '__main__':
    unittest.main()
