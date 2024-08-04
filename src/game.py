"""Module providing the Game class."""

from dataclasses import dataclass

from action import Action
from state import State

@dataclass
class Game:
    """Class representing a game, which is a particular type of search problem."""
    
    initial_state: State

    def actions(self, s: State) -> list[Action]:
        legal_actions: list[Action] = []
        
        for m in s.board.legal_moves:
            legal_actions.append(Action(m))

        return legal_actions
    
    def result(self, s: State, a: Action) -> State:
        board = s.board.copy()
        board.push(a.move)
        sp = State(board)

        return sp
    
    def terminal_test(self, s: State) -> bool:
        return s.board.is_game_over()
    
    def utility(self, s: State, p: bool) -> float:
        outcome = s.board.outcome()
        
        if outcome.winner == p:
            return float('inf')

        return 0
