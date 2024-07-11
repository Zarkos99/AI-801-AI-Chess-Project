import unittest
from ChessEnums import Space
from Coord import Coord

class TestCoord(unittest.TestCase):
    def test_initialization(self):
        coord = Coord(3, 4)
        self.assertEqual(coord.c, 3)
        self.assertEqual(coord.r, 4)

    def test_fromSpace(self):
        coord = Coord.fromSpace(Space.D4)
        self.assertEqual(coord.c, 3)  # D is the 4th column, 0-indexed as 3
        self.assertEqual(coord.r, 3)  # 4 is the 4th row, 0-indexed as 3

    def test_toSpace(self):
        coord = Coord(3, 3)
        self.assertEqual(coord.toSpace(), Space.D4)

    def test_isValid(self):
        valid_coord = Coord(3, 4)
        invalid_coord_c = Coord(-1, 4)
        invalid_coord_r = Coord(3, 8)
        self.assertTrue(valid_coord.isValid())
        self.assertFalse(invalid_coord_c.isValid())
        self.assertFalse(invalid_coord_r.isValid())

    def test_edge_cases(self):
        edge_coord_1 = Coord(0, 0)
        edge_coord_2 = Coord(7, 7)
        self.assertTrue(edge_coord_1.isValid())
        self.assertTrue(edge_coord_2.isValid())
        self.assertEqual(edge_coord_1.toSpace(), Space.A1)
        self.assertEqual(edge_coord_2.toSpace(), Space.H8)
        self.assertEqual(Coord.fromSpace(Space.A1), edge_coord_1)
        self.assertEqual(Coord.fromSpace(Space.H8), edge_coord_2)

if __name__ == '__main__':
    unittest.main()
