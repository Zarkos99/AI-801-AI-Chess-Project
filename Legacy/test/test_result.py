import unittest
from ChessPiece import ChessPiece
from ChessEnums import Piece_Type, Player, Space
from State import State
from Action import Action
from Result import Result

class TestResultFunction(unittest.TestCase):

    def setUp(self):
        self.initial_state = State()

    def test_normal_move(self):
        action = Action(Space.E2, Space.E4)
        new_state = Result(self.initial_state, action)
        self.assertEqual(new_state.board[Space.E4.value].piece_type, Piece_Type.PAWN)
        self.assertEqual(new_state.board[Space.E2.value].piece_type, Piece_Type.___)

    def test_capture(self):
        self.initial_state.board[Space.D5.value] = ChessPiece(Piece_Type.PAWN, Player.BLACK)
        action = Action(Space.D4, Space.D5)
        new_state = Result(self.initial_state, action)
        self.assertEqual(new_state.board[Space.D5.value].piece_type, Piece_Type.___)
        self.assertEqual(new_state.board[Space.D5.value].color, Player.___)
        self.assertEqual(new_state.board[Space.D4.value].piece_type, Piece_Type.___)

    def test_en_passant(self):
        self.initial_state.board[Space.E5.value] = ChessPiece(Piece_Type.PAWN, Player.WHITE)
        self.initial_state.board[Space.D5.value] = ChessPiece(Piece_Type.PAWN, Player.BLACK)
        action = Action(Space.E5, Space.D6)
        new_state = Result(self.initial_state, action)
        self.assertEqual(new_state.board[Space.D6.value].piece_type, Piece_Type.PAWN)
        self.assertEqual(new_state.board[Space.D6.value].color, Player.WHITE)
        self.assertEqual(new_state.board[Space.D5.value].piece_type, Piece_Type.___)

    def test_castling_kingside(self):
        action = Action(Space.E1, Space.G1)
        new_state = Result(self.initial_state, action)
        self.assertEqual(new_state.board[Space.G1.value].piece_type, Piece_Type.KING)
        self.assertEqual(new_state.board[Space.G1.value].color, Player.WHITE)
        self.assertEqual(new_state.board[Space.F1.value].piece_type, Piece_Type.ROOK)
        self.assertEqual(new_state.board[Space.F1.value].color, Player.WHITE)
        self.assertEqual(new_state.board[Space.E1.value].piece_type, Piece_Type.___)
        self.assertEqual(new_state.board[Space.H1.value].piece_type, Piece_Type.___)

    def test_promotion(self):
        self.initial_state.board[Space.E7.value] = ChessPiece(Piece_Type.PAWN, Player.WHITE)
        action = Action(Space.E7, Space.E8, par_promotion=Piece_Type.QUEEN)
        new_state = Result(self.initial_state, action)
        self.assertEqual(new_state.board[Space.E8.value].piece_type, Piece_Type.QUEEN)
        self.assertEqual(new_state.board[Space.E8.value].color, Player.WHITE)

    def test_check(self):
        self.initial_state.board[Space.D4.value] = ChessPiece(Piece_Type.ROOK, Player.BLACK)
        action = Action(Space.D4, Space.E4)
        new_state = Result(self.initial_state, action)
        self.assertFalse(new_state.check)

if __name__ == '__main__':
    unittest.main()
