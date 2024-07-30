"""Module providing the minimax function."""

from action import Action
from actions import Actions
from state import State
from terminal_test import TerminalTest
from transition_model import TransitionModel
from utility_function import UtilityFunction

terminal_test = TerminalTest()
utility = UtilityFunction()
actions = Actions()
result = TransitionModel()

def minimax(state: State) -> Action:
    """Function computing the minimax decision from the current state."""

    return max(actions(state), key=lambda a: min_value(result(state, a)))

def max_value(state: State) -> float:
    """Function implementing the max part of the minimax algorithm."""

    if terminal_test(state):
        return utility(state)

    v = float('-inf')

    for a in actions(state):
        v = max(v, min_value(result(state, a)))

    return v

def min_value(state: State) -> float:
    """Function implementing the min part of the minimax algorithm."""

    if terminal_test(state):
        return utility(state)

    v = float('inf')

    for a in actions(state):
        v = min(v, max_value(result(state, a)))

    return v
