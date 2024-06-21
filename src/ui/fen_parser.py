"""A util to parse a fen string for the UI"""

import unittest

class ChessPiece:
    """Defines a UI Chess Piece"""
    def __init__(self, piece_type, color):
        self.piece_type = piece_type
        self.color = color

    def __repr__(self):
        return f"{self.color}{self.piece_type}"

def parse_fen(fen):
    """Parse a FEN (Forsyth-Edwards Notation) string into an array of pieces"""
    piece_mapping = {
        'p': 'pawn', 'r': 'rook', 'n': 'knight', 'b': 'bishop', 'q': 'queen', 'k': 'king',
        'P': 'pawn', 'R': 'rook', 'N': 'knight', 'B': 'bishop', 'Q': 'queen', 'K': 'king'
    }
    color_mapping = {
        'p': 'black', 'r': 'black', 'n': 'black', 'b': 'black', 'q': 'black', 'k': 'black',
        'P': 'white', 'R': 'white', 'N': 'white', 'B': 'white', 'Q': 'white', 'K': 'white'
    }

    rows = fen.split(' ')[0].split('/')
    board = []

    for row in rows:
        board_row = []
        for char in row:
            if char.isdigit():
                board_row.extend([None] * int(char))
            else:
                piece_type = piece_mapping[char]
                color = color_mapping[char]
                board_row.append(ChessPiece(piece_type, color))
        board.append(board_row)

    return board

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

    def test_invalid_fen(self):
        with self.assertRaises(KeyError):
            parse_fen("9/8/8/8/8/8/8/8")

if __name__ == '__main__':
    unittest.main()
