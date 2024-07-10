import unittest
from unittest.mock import MagicMock
from ChessEnums import Player, Piece_Type
import State
from PathCost import PathCost

class TestPathCost(unittest.TestCase):
    def setUp(self):
        self.mock_state = MagicMock(spec=State)

    def test_path_cost_white_player(self):
        # Setup mock state for a white player with specific pieces
        self.mock_state.player = Player.WHITE
        self.mock_state.board = [
            MagicMock(color=Player.WHITE, piece_type=Piece_Type.PAWN),
            MagicMock(color=Player.BLACK, piece_type=Piece_Type.PAWN),
            MagicMock(color=Player.WHITE, piece_type=Piece_Type.ROOK),
            MagicMock(color=Player.BLACK, piece_type=Piece_Type.QUEEN)
        ]
        path_cost = PathCost(self.mock_state)
        expected_piece_weight = (1 + 5) / (1 + 9)  # 6 / 10 = 0.6
        self.assertAlmostEqual(float(path_cost), expected_piece_weight, delta=0.01)

    def test_path_cost_black_player(self):
        # Setup mock state for a black player with specific pieces
        self.mock_state.player = Player.BLACK
        self.mock_state.board = [
            MagicMock(color=Player.WHITE, piece_type=Piece_Type.PAWN),
            MagicMock(color=Player.BLACK, piece_type=Piece_Type.PAWN),
            MagicMock(color=Player.WHITE, piece_type=Piece_Type.ROOK),
            MagicMock(color=Player.BLACK, piece_type=Piece_Type.QUEEN)
        ]
        path_cost = PathCost(self.mock_state)
        expected_piece_weight = (1 + 9) / (1 + 5)  # 10 / 6 = 1.6667
        self.assertAlmostEqual(float(path_cost), expected_piece_weight, delta=0.01)

    def test_path_cost_division_by_zero_white(self):
        # Setup mock state for a white player with no black pieces
        self.mock_state.player = Player.WHITE
        self.mock_state.board = [
            MagicMock(color=Player.WHITE, piece_type=Piece_Type.PAWN),
            MagicMock(color=Player.WHITE, piece_type=Piece_Type.ROOK)
        ]
        path_cost = PathCost(self.mock_state)
        self.assertEqual(float(path_cost), float('inf'))

    def test_path_cost_division_by_zero_black(self):
        # Setup mock state for a black player with no white pieces
        self.mock_state.player = Player.BLACK
        self.mock_state.board = [
            MagicMock(color=Player.BLACK, piece_type=Piece_Type.PAWN),
            MagicMock(color=Player.BLACK, piece_type=Piece_Type.ROOK)
        ]
        path_cost = PathCost(self.mock_state)
        self.assertEqual(float(path_cost), float('inf'))

    def test_path_cost_expanded_no_children(self):
        # Setup mock state with pieces and set expanded to True
        self.mock_state.player = Player.WHITE
        self.mock_state.board = [
            MagicMock(color=Player.WHITE, piece_type=Piece_Type.PAWN),
            MagicMock(color=Player.BLACK, piece_type=Piece_Type.PAWN)
        ]
        path_cost = PathCost(self.mock_state)
        path_cost.expanded = True
        self.assertEqual(float(path_cost), 0.0)

    def test_path_cost_expanded_with_children(self):
        # Setup mock state with pieces and set expanded to True with children
        self.mock_state.player = Player.WHITE
        self.mock_state.board = [
            MagicMock(color=Player.WHITE, piece_type=Piece_Type.PAWN),
            MagicMock(color=Player.BLACK, piece_type=Piece_Type.PAWN)
        ]
        path_cost = PathCost(self.mock_state)
        path_cost.expanded = True
        path_cost.child_count = 2
        path_cost.min_child_cost = 4.0
        self.assertEqual(float(path_cost), 1.0 / 4.0)

if __name__ == '__main__':
    unittest.main()
