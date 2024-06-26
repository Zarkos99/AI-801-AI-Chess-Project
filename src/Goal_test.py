"""Checks that a game is in check"""
from state import State
# Could maybe also live in Utility Functions
def goal_test(game_state: State) -> bool:
    """simple helper to see if the game is in check"""
    return game_state.check
