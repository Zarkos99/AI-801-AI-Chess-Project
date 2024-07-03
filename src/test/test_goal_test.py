import unittest
from unittest.mock import MagicMock
from Goal_test import goal_test

class TestGoalTest(unittest.TestCase):

    def test_goal_reached(self):
        # Create a mock state where check returns True
        gameState = MagicMock()
        gameState.check = True

        # Assert that goal_test returns True
        self.assertTrue(goal_test(gameState))

    def test_goal_not_reached(self):
        # Create a mock state where check returns False
        gameState = MagicMock()
        gameState.check = False

        # Assert that goal_test returns False
        self.assertFalse(goal_test(gameState))

if __name__ == '__main__':
    unittest.main()
