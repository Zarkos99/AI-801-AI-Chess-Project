import unittest
from ChessEnums import Piece_Type, Player
from ChessPiece import ChessPiece

class TestChessPiece(unittest.TestCase):
    def test_initialization_default(self):
        piece = ChessPiece()
        self.assertEqual(piece.piece_type, Piece_Type.___)
        self.assertEqual(piece.color, Player.___)

    def test_initialization_custom(self):
        piece = ChessPiece(Piece_Type.QUEEN, Player.WHITE)
        self.assertEqual(piece.piece_type, Piece_Type.QUEEN)
        self.assertEqual(piece.color, Player.WHITE)

    def test_repr(self):
        piece = ChessPiece(Piece_Type.KNIGHT, Player.BLACK)
        self.assertEqual(repr(piece), f"{Player.BLACK}{Piece_Type.KNIGHT}")

    def test_equality(self):
        piece1 = ChessPiece(Piece_Type.ROOK, Player.WHITE)
        piece2 = ChessPiece(Piece_Type.ROOK, Player.WHITE)
        piece3 = ChessPiece(Piece_Type.BISHOP, Player.BLACK)
        self.assertEqual(piece1, piece2)
        self.assertNotEqual(piece1, piece3)

    def test_inequality_different_type(self):
        piece = ChessPiece(Piece_Type.PAWN, Player.BLACK)
        self.assertNotEqual(piece, "not a chess piece")

if __name__ == '__main__':
    unittest.main()
