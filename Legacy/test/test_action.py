import unittest
from Action import Action
from ChessEnums import Space, Piece_Type

class TestAction(unittest.TestCase):
    def test_default_action(self):
        action = Action()
        self.assertEqual(action.orig, Space.A1)
        self.assertEqual(action.dest, Space.A1)
        self.assertEqual(action.promotion, Piece_Type.___)

    def test_custom_action(self):
        action = Action(Space.B1, Space.C1, Piece_Type.QUEEN)
        self.assertEqual(action.orig, Space.B1)
        self.assertEqual(action.dest, Space.C1)
        self.assertEqual(action.promotion, Piece_Type.QUEEN)

    def test_equality(self):
        action1 = Action(Space.A1, Space.B1, Piece_Type.KNIGHT)
        action2 = Action(Space.A1, Space.B1, Piece_Type.KNIGHT)
        action3 = Action(Space.B1, Space.A1, Piece_Type.QUEEN)
        self.assertEqual(action1, action2)
        self.assertNotEqual(action1, action3)

    def test_inequality_different_type(self):
        action = Action(Space.A1, Space.B1, Piece_Type.KNIGHT)
        self.assertNotEqual(action, "not an action")

    def test_edge_cases(self):
        action1 = Action(Space.C1, Space.A1, Piece_Type.BISHOP)
        action2 = Action(Space.C1, Space.A1, Piece_Type.BISHOP)
        self.assertEqual(action1, action2)
        action3 = Action(Space.C1, Space.A1, Piece_Type.___)
        self.assertNotEqual(action1, action3)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            Action(Space.A1, None, Piece_Type.QUEEN)  # Invalid destination
        with self.assertRaises(ValueError):
            Action(None, Space.A1, Piece_Type.KNIGHT)  # Invalid origin
        with self.assertRaises(ValueError):
            Action(Space.A1, Space.B1, None)  # Invalid promotion

    def test_all_combinations(self):
        spaces = [Space.D1, Space.E1, Space.F1]
        pieces = [Piece_Type.QUEEN, Piece_Type.KNIGHT, Piece_Type.___, Piece_Type.BISHOP]
        for orig in spaces:
            for dest in spaces:
                for promotion in pieces:
                    action = Action(orig, dest, promotion)
                    self.assertEqual(action.orig, orig)
                    self.assertEqual(action.dest, dest)
                    self.assertEqual(action.promotion, promotion)

if __name__ == '__main__':
    unittest.main()