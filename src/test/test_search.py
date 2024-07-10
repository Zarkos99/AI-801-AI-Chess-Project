import unittest
from time import time

from ChessPiece import ChessPiece
from Action import Action
from State import State
from Search import Search

class TestSearchFunction(unittest.TestCase):

    def setUp(self):
        # Setup any initial states or configurations here
        self.initial_state = State()  # Assuming State initializes to a standard chess starting position

    def test_search_basic(self):
        # Basic functionality test
        action = Search(self.initial_state, par_seconds=5.0)
        self.assertIsInstance(action, Action)

    def test_search_within_time(self):
        # Ensure the search respects the time constraint
        start = time()
        action = Search(self.initial_state, par_seconds=2.0)
        end = time()
        self.assertTrue(end - start <= 2.0 + 0.1)  # Allowing a small margin for processing overhead

    def test_search_no_actions(self):
        # Test handling of an initial state with no possible actions
        empty_state = State()
        empty_state.board = [ChessPiece()] * 64  # Assuming this represents an empty board
        action = Search(empty_state, par_seconds=5.0)
        self.assertEqual(action, Action())  # Assuming the function returns the default action

if __name__ == '__main__':
    unittest.main()
