"""Tests for parsefen"""
import unittest
from parse_fen import parse_fen

class TestParseFen(unittest.TestCase):
    """Simple unit test for parse_fen"""

    def test_initial_position(self):
        """Tests default board state"""
        fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
        board = parse_fen(fen)
        self.assertEqual(repr(board[0][0]), 'blackrook')
        self.assertEqual(repr(board[0][1]), 'blackknight')
        self.assertEqual(repr(board[0][2]), 'blackbishop')
        self.assertEqual(repr(board[0][3]), 'blackqueen')
        self.assertEqual(repr(board[0][4]), 'blackking')
        self.assertEqual(repr(board[0][5]), 'blackbishop')
        self.assertEqual(repr(board[0][6]), 'blackknight')
        self.assertEqual(repr(board[0][7]), 'blackrook')
        self.assertEqual(repr(board[1][0]), 'blackpawn')
        self.assertEqual(repr(board[7][0]), 'whiterook')
        self.assertEqual(repr(board[6][0]), 'whitepawn')
        self.assertIsNone(board[4][4])

    def test_empty_board(self):
        """Tests empty board state"""
        fen = "8/8/8/8/8/8/8/8"
        board = parse_fen(fen)
        for row in board:
            for piece in row:
                self.assertIsNone(piece)

    def test_mixed_position(self):
        """Tests random board state"""
        fen = "8/8/4P3/8/3p4/8/8/8"
        board = parse_fen(fen)
        self.assertEqual(repr(board[2][4]), 'whitepawn')
        self.assertEqual(repr(board[4][3]), 'blackpawn')
        self.assertIsNone(board[0][0])
        self.assertIsNone(board[7][7])

if __name__ == '__main__':
    unittest.main()
