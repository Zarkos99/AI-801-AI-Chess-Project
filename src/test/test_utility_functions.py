import unittest
import numpy as np
from ChessEnums import Player, Piece_Type, Space
from ChessPiece import ChessPiece
from Coord import Coord
from UtilityFunctions import (
    IsCheckForPlayer, IsEmpty, IsOpponentPiece, IsPiece, IsPlayerPiece,
    ForEachSpaceHorizontalAndVertical, ForEachSpaceDiagonal, ForEachSpaceL,
    ToPlayer, mapFenCharToPiece, mapPgnCharToPiece
)

class TestChessFunctions(unittest.TestCase):

    def setUp(self):
        self.board = np.full(64, ChessPiece(Piece_Type.___, None), dtype=object)

        # Set up pieces on the board
        self.board[0] = ChessPiece(Piece_Type.ROOK, Player.WHITE)
        self.board[1] = ChessPiece(Piece_Type.KNIGHT, Player.WHITE)
        self.board[2] = ChessPiece(Piece_Type.BISHOP, Player.WHITE)
        self.board[3] = ChessPiece(Piece_Type.QUEEN, Player.WHITE)
        self.board[4] = ChessPiece(Piece_Type.KING, Player.WHITE)
        self.board[5] = ChessPiece(Piece_Type.BISHOP, Player.WHITE)
        self.board[6] = ChessPiece(Piece_Type.KNIGHT, Player.WHITE)
        self.board[7] = ChessPiece(Piece_Type.ROOK, Player.WHITE)

        self.board[56] = ChessPiece(Piece_Type.ROOK, Player.BLACK)
        self.board[57] = ChessPiece(Piece_Type.KNIGHT, Player.BLACK)
        self.board[58] = ChessPiece(Piece_Type.BISHOP, Player.BLACK)
        self.board[59] = ChessPiece(Piece_Type.QUEEN, Player.BLACK)
        self.board[60] = ChessPiece(Piece_Type.KING, Player.BLACK)
        self.board[61] = ChessPiece(Piece_Type.BISHOP, Player.BLACK)
        self.board[62] = ChessPiece(Piece_Type.KNIGHT, Player.BLACK)
        self.board[63] = ChessPiece(Piece_Type.ROOK, Player.BLACK)

#    def test_IsCheckForPlayer(self):
 #       self.assertFalse(IsCheckForPlayer(self.board, Player.WHITE, Space.A4))
  #      self.board[52] = ChessPiece(Piece_Type.QUEEN, Player.BLACK)
   #     self.assertTrue(IsCheckForPlayer(self.board, Player.WHITE, Space.A4))

    def test_IsEmpty(self):
        self.assertTrue(IsEmpty(ChessPiece(Piece_Type.___, None)))
        self.assertFalse(IsEmpty(ChessPiece(Piece_Type.PAWN, Player.WHITE)))

    def test_IsOpponentPiece(self):
        self.assertTrue(IsOpponentPiece(ChessPiece(Piece_Type.ROOK, Player.BLACK), Player.WHITE))
        self.assertFalse(IsOpponentPiece(ChessPiece(Piece_Type.ROOK, Player.WHITE), Player.WHITE))
        self.assertFalse(IsOpponentPiece(ChessPiece(Piece_Type.___, None), Player.WHITE))

    def test_IsPiece(self):
        self.assertTrue(IsPiece(ChessPiece(Piece_Type.PAWN, Player.WHITE)))
        self.assertFalse(IsPiece(ChessPiece(Piece_Type.___, None)))

    def test_IsPlayerPiece(self):
        self.assertTrue(IsPlayerPiece(ChessPiece(Piece_Type.ROOK, Player.WHITE), Player.WHITE))
        self.assertFalse(IsPlayerPiece(ChessPiece(Piece_Type.ROOK, Player.BLACK), Player.WHITE))
        self.assertFalse(IsPlayerPiece(ChessPiece(Piece_Type.___, None), Player.WHITE))

    def test_ForEachSpaceHorizontalAndVertical(self):
        spaces = []

        def collect_spaces(space):
            spaces.append(space)

        ForEachSpaceHorizontalAndVertical(collect_spaces, 28, self.board)  # 28 represents D4
        self.assertGreater(len(spaces), 0)

    def test_ForEachSpaceDiagonal(self):
        spaces = []

        def collect_spaces(space):
            spaces.append(space)

        ForEachSpaceDiagonal(collect_spaces, 28, self.board)  # 28 represents D4
        self.assertGreater(len(spaces), 0)

    def test_ForEachSpaceL(self):
        spaces = []

        def collect_spaces(space):
            spaces.append(space)

        ForEachSpaceL(collect_spaces, 28)  # 28 represents D4
        self.assertGreater(len(spaces), 0)

    def test_ToPlayer(self):
        self.assertEqual(ToPlayer(ChessPiece(Piece_Type.ROOK, Player.WHITE)), Player.WHITE)
        self.assertEqual(ToPlayer(ChessPiece(Piece_Type.ROOK, Player.BLACK)), Player.BLACK)

    def test_mapFenCharToPiece(self):
        piece = mapFenCharToPiece('R')
        self.assertEqual(piece.piece_type, Piece_Type.ROOK)
        self.assertEqual(piece.color, Player.WHITE)

        piece = mapFenCharToPiece('r')
        self.assertEqual(piece.piece_type, Piece_Type.ROOK)
        self.assertEqual(piece.color, Player.BLACK)

    def test_mapPgnCharToPiece(self):
        self.assertEqual(mapPgnCharToPiece('P', Player.WHITE), Piece_Type.PAWN)
        self.assertEqual(mapPgnCharToPiece('R', Player.BLACK), Piece_Type.ROOK)
        self.assertEqual(mapPgnCharToPiece('N', Player.WHITE), Piece_Type.KNIGHT)
        self.assertEqual(mapPgnCharToPiece('B', Player.BLACK), Piece_Type.BISHOP)
        self.assertEqual(mapPgnCharToPiece('Q', Player.WHITE), Piece_Type.QUEEN)
        self.assertEqual(mapPgnCharToPiece('K', Player.BLACK), Piece_Type.KING)

if __name__ == '__main__':
    unittest.main()