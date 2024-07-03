import unittest
from ChessEnums import Piece_Type, Player, Space, Piece_Type_FIRST, Piece_Type_LAST
from enum import Enum, IntEnum

class TestEnums(unittest.TestCase):

    def test_Player_enum(self):
        self.assertTrue(issubclass(Player, Enum))
        self.assertEqual(Player.__members__, {
            '___': Player.___,
            'WHITE': Player.WHITE,
            'BLACK': Player.BLACK
        })

    def test_Piece_Type_enum(self):
        self.assertTrue(issubclass(Piece_Type, Enum))
        self.assertEqual(Piece_Type.__members__, {
            '___': Piece_Type.___,
            'PAWN': Piece_Type.PAWN,
            'ROOK': Piece_Type.ROOK,
            'KNIGHT': Piece_Type.KNIGHT,
            'BISHOP': Piece_Type.BISHOP,
            'QUEEN': Piece_Type.QUEEN,
            'KING': Piece_Type.KING
        })
        self.assertEqual(Piece_Type_FIRST, Piece_Type.___)
        self.assertEqual(Piece_Type_LAST, Piece_Type.KING)

    def test_Space_enum(self):
        self.assertTrue(issubclass(Space, IntEnum))
        self.assertEqual(len(Space), 64)  # Check number of members

    def test_Space_enum_values(self):
        # Check a few selected values to ensure correctness
        self.assertEqual(Space.A1.value, 0)
        self.assertEqual(Space.A8.value, 7)
        self.assertEqual(Space.H1.value, 7 * 8)
        self.assertEqual(Space.H8.value, 7 * 8 + 7)

if __name__ == '__main__':
    unittest.main()