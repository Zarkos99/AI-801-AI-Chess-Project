import unittest
from ChessEnums import Space, Piece_Type, Player
from ChessPiece import ChessPiece
from State import State

class TestStateInitialization(unittest.TestCase):

    def setUp(self):
        self.state = State()

    def test_board_initialization(self):
        board = self.state.board

        # Test for white pieces
        self.assertEqual(board[Space.A2], ChessPiece(Piece_Type.PAWN, Player.WHITE))
        self.assertEqual(board[Space.B2], ChessPiece(Piece_Type.PAWN, Player.WHITE))
        self.assertEqual(board[Space.C2], ChessPiece(Piece_Type.PAWN, Player.WHITE))
        self.assertEqual(board[Space.D2], ChessPiece(Piece_Type.PAWN, Player.WHITE))
        self.assertEqual(board[Space.E2], ChessPiece(Piece_Type.PAWN, Player.WHITE))
        self.assertEqual(board[Space.F2], ChessPiece(Piece_Type.PAWN, Player.WHITE))
        self.assertEqual(board[Space.G2], ChessPiece(Piece_Type.PAWN, Player.WHITE))
        self.assertEqual(board[Space.H2], ChessPiece(Piece_Type.PAWN, Player.WHITE))
        self.assertEqual(board[Space.B1], ChessPiece(Piece_Type.KNIGHT, Player.WHITE))
        self.assertEqual(board[Space.G1], ChessPiece(Piece_Type.KNIGHT, Player.WHITE))
        self.assertEqual(board[Space.C1], ChessPiece(Piece_Type.BISHOP, Player.WHITE))
        self.assertEqual(board[Space.F1], ChessPiece(Piece_Type.BISHOP, Player.WHITE))
        self.assertEqual(board[Space.A1], ChessPiece(Piece_Type.ROOK, Player.WHITE))
        self.assertEqual(board[Space.H1], ChessPiece(Piece_Type.ROOK, Player.WHITE))
        self.assertEqual(board[Space.D1], ChessPiece(Piece_Type.QUEEN, Player.WHITE))
        self.assertEqual(board[Space.E1], ChessPiece(Piece_Type.KING, Player.WHITE))

        # Test for black pieces
        self.assertEqual(board[Space.A7], ChessPiece(Piece_Type.PAWN, Player.BLACK))
        self.assertEqual(board[Space.B7], ChessPiece(Piece_Type.PAWN, Player.BLACK))
        self.assertEqual(board[Space.C7], ChessPiece(Piece_Type.PAWN, Player.BLACK))
        self.assertEqual(board[Space.D7], ChessPiece(Piece_Type.PAWN, Player.BLACK))
        self.assertEqual(board[Space.E7], ChessPiece(Piece_Type.PAWN, Player.BLACK))
        self.assertEqual(board[Space.F7], ChessPiece(Piece_Type.PAWN, Player.BLACK))
        self.assertEqual(board[Space.G7], ChessPiece(Piece_Type.PAWN, Player.BLACK))
        self.assertEqual(board[Space.H7], ChessPiece(Piece_Type.PAWN, Player.BLACK))
        self.assertEqual(board[Space.B8], ChessPiece(Piece_Type.KNIGHT, Player.BLACK))
        self.assertEqual(board[Space.G8], ChessPiece(Piece_Type.KNIGHT, Player.BLACK))
        self.assertEqual(board[Space.C8], ChessPiece(Piece_Type.BISHOP, Player.BLACK))
        self.assertEqual(board[Space.F8], ChessPiece(Piece_Type.BISHOP, Player.BLACK))
        self.assertEqual(board[Space.A8], ChessPiece(Piece_Type.ROOK, Player.BLACK))
        self.assertEqual(board[Space.H8], ChessPiece(Piece_Type.ROOK, Player.BLACK))
        self.assertEqual(board[Space.D8], ChessPiece(Piece_Type.QUEEN, Player.BLACK))
        self.assertEqual(board[Space.E8], ChessPiece(Piece_Type.KING, Player.BLACK))

    def test_other_attributes_initialization(self):
        state = self.state

        allFalse = {
            Player.WHITE: False,
            Player.BLACK: False
        }

        self.assertEqual(state.moves, [])
        self.assertEqual(state.king_space, { Player.WHITE: Space.E1, Player.BLACK: Space.E8})
        self.assertEqual(state.king_moved, allFalse)
        self.assertEqual(state.rookA_moved, allFalse)
        self.assertEqual(state.rookH_moved, allFalse)
        self.assertEqual(state.player, Player.WHITE)
        self.assertFalse(state.check)

if __name__ == '__main__':
    unittest.main()

