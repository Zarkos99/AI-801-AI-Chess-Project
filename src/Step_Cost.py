from state import State
from action import Action

def step_cost(game_state: State, player_move: Action) -> float:
    """ The intent is that if a guaranteed victory is found,
        the cost of every parent in that move sequence is updated to 0
        (so that it will always be the lowest cost).
        If a move leads to guaranteed defeat, its cost is infinite,
        so it is never chosen. Anything in between,
        the path cost is estimated using the number of moves you have
        compared to the number of moves the opponent has,
        as well as the ratio of pieces controlled by both players.
        0 - best choice gets to check state...
        ratio "score" of effectivness
        inf - ends in defeat.."""
    new_game_state = game_state
    #gets game to check state
    if new_game_state.check:
        return 0

    # results in favorable outcome for user
    return 1

    # results in loss
    # return inf
