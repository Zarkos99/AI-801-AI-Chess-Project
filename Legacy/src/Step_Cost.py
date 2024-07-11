import State
import Action

# Basically the intent is that if a guaranteed victory is found, the cost of every parent in that move sequence is updated to 0 (so that it will always be the lowest cost). If a move leads to guaranteed defeat, its cost is infinite, so it is never chosen. Anything in between, the path cost is estimated using the number of moves you have compared to the number of moves the opponent has, as well as the ratio of pieces controlled by both players.
# 0 - best choice gets to check state...
# ratio "score" of effectivness
# inf - ends in defeat..


def step_cost(gameState: State, playerMove: Action) -> float:
    # TODO eval move
    newGameState = gameState
    # gets game to check state
    if (newGameState.check):
        return 0

    # results in favorable outcome for user
    return 1

    # results in loss
    return inf
