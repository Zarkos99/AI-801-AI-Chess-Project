"""Module providing the alpha_beta_search function."""

from action import Action
from actions import Actions
from state import State
from terminal_test import TerminalTest
from transition_model import TransitionModel
from utility_function import UtilityFunction

actions = Actions()
result = TransitionModel()
terminal_test = TerminalTest()
utility = UtilityFunction()

def alpha_beta_search(state: State) -> Action:
    """Function implementing a minimax search with alpha-beta pruning."""

    v = max_value(state, float('-inf'), float('inf'))

    return v[1]

def max_value(state: State, alpha: float, beta: float) -> tuple[float, Action]:
    """Function implementing the max part of alpha_beta_search."""

    if terminal_test(state):
        return (utility(state), None)

    v = (float('-inf'), None)

    for a in actions(state):
        v = max(v, (min_value(result(state, a), alpha, beta)[0], a), key=lambda w: w[0])

        if v[0] >= beta:
            return v

        alpha = max(alpha, v[0])

    return v

def min_value(state: State, alpha: float, beta: float) -> tuple[float, Action]:
    """Function implementing the min part of alpha_beta_search."""

    if terminal_test(state):
        return (utility(state), None)

    v = (float('inf'), None)

    for a in actions(state):
        v = min(v, (max_value(result(state, a), alpha, beta), a), key=lambda w: w[0])

        if v[0] <= alpha:
            return v

        beta = min(beta, v[0])

    return v
