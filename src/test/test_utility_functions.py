import unittest
import numpy as np
from ChessEnums import Player, Space, Piece_Type

from UtilityFunctions import IsCheckForPlayer, IsEmpty, IsOpponentPiece, IsPiece
from UtilityFunctions import IsPlayerPiece, ForEachSpaceHorizontalAndVertical, ForEachSpaceDiagonal
from UtilityFunctions import ForEachSpaceL, ToPlayer, mapFenCharToPiece, mapPgnCharToPiece

class TestChessUtilities(unittest.TestCase):

    def setUp(self):
        self.board = np.full((8, 8), Piece_Type.___, dtype=Piece_Type)

    def test_IsCheckForPlayer(self):
        # Set up a simple check scenario
        self.board[0][0] = Piece_Type.KING
        self.board[0][7] = Piece_Type.ROOK
        self.assertTrue(IsCheckForPlayer(self.board, Player.WHITE, Space.A1))

        self.board[0][7] = Piece_Type.___
        self.assertFalse(IsCheckForPlayer(self.board, Player.WHITE, Space.A1))

    def test_IsEmpty(self):
        self.assertTrue(IsEmpty(Piece_Type.___))
        self.assertFalse(IsEmpty(Piece_Type.PAWN))

    def test_IsOpponentPiece(self):
        self.assertTrue(IsOpponentPiece(Piece_Type.B_P, Player.WHITE))
        self.assertFalse(IsOpponentPiece(Piece_Type.W_P, Player.WHITE))
        self.assertFalse(IsOpponentPiece(Piece_Type.___, Player.WHITE))

    def test_IsPiece(self):
        self.assertTrue(IsPiece(Piece_Type.PAWN))
        self.assertFalse(IsPiece(Piece_Type.___))

    def test_IsPlayerPiece(self):
        self.assertTrue(IsPlayerPiece(Piece_Type.W_P, Player.WHITE))
        self.assertFalse(IsPlayerPiece(Piece_Type.B_P, Player.WHITE))
        self.assertFalse(IsPlayerPiece(Piece_Type.___, Player.WHITE))

    def test_ForEachSpaceHorizontalAndVertical(self):
        visited = set()

        def func(space):
            visited.add(space)

        ForEachSpaceHorizontalAndVertical(func, Space.A1, self.board)
        expected_spaces = {Space.A2, Space.A3, Space.A4, Space.A5, Space.A6, Space.A7, Space.A8,
                           Space.B1, Space.C1, Space.D1, Space.E1, Space.F1, Space.G1, Space.H1}
        self.assertEqual(visited, expected_spaces)

    def test_ForEachSpaceDiagonal(self):
        visited = set()

        def func(space):
            visited.add(space)

        ForEachSpaceDiagonal(func, Space.D4, self.board)
        expected_spaces = {Space.A1, Space.B2, Space.C3, Space.E5, Space.F6, Space.G7, Space.H8,
                           Space.G1, Space.F2, Space.E3, Space.C5, Space.B6, Space.A7}
        self.assertEqual(visited, expected_spaces)

    def test_ForEachSpaceL(self):
        visited = set()

        def func(space):
            visited.add(space)

        ForEachSpaceL(func, Space.D4, self.board)
        expected_spaces = {Space.B3, Space.B5, Space.C2, Space.C6, Space.E2, Space.E6, Space.F3, Space.F5}
        self.assertEqual(visited, expected_spaces)

    def test_ToPlayer(self):
        self.assertEqual(ToPlayer(Piece_Type.W_P), Player.WHITE)
        self.assertEqual(ToPlayer(Piece_Type.B_P), Player.BLACK)

    def test_mapFenCharToPiece(self):
        piece = mapFenCharToPiece('p')
        self.assertEqual(piece.piece_type, Piece_Type.PAWN)
        self.assertEqual(piece.player, Player.BLACK)

        piece = mapFenCharToPiece('P')
        self.assertEqual(piece.piece_type, Piece_Type.PAWN)
        self.assertEqual(piece.player, Player.WHITE)

    def test_mapPgnCharToPiece(self):
        piece = mapPgnCharToPiece('P', Player.WHITE)
        self.assertEqual(piece, Piece_Type.PAWN)

        piece = mapPgnCharToPiece('R', Player.BLACK)
        self.assertEqual(piece, Piece_Type.B_R)


if __name__ == '__main__':
    unittest.main()
