"""Module providing the AgentFunction class."""

from dataclasses import dataclass, field
from typing import Tuple, Dict

from action import Action
from percept_sequence import PerceptSequence
from chess_puzzle_data import obtain_latest_daily_puzzle

@dataclass
class AgentFunction:
    """Class representing an agent function, which is an abstract mathematical description of an
       agent's behavior that maps any given percept sequence to an action."""
    partial_table: Dict[Tuple[str, ...], Action] = field(default_factory=dict)

    def __call__(self, percept_sequence: PerceptSequence) -> Action:
        return self.partial_table.get(percept_sequence, "No action found")

    @classmethod
    def processGame(cls, game):
        partial_table: Dict[Tuple[str, ...], Action] = {}

        board = game.board()
        percept_sequence = []
        node = game

        while node.variations:
            next_node = node.variation(0)
            move = next_node.move
            percept_sequence.append(board.san(move))
            board.push(move)

            if len(percept_sequence) > 1:  # Ensure we have a previous percept to map the action to
                # The percept sequence up to the current move maps to the current move (action)
                partial_table[tuple(percept_sequence[:-1])] = percept_sequence[-1]

            node = next_node

        # Am I doing somethign wrong here? I feel like this should not be needed
        if not hasattr(cls, 'partial_table'):
            cls.partial_table = {}
        cls.partial_table.update(partial_table)


# Use Kostis daily puzzle data parsed game
AgentFunction.processGame(obtain_latest_daily_puzzle().game)
agent = AgentFunction()

percept_sequence = ("e4", "e5", "Nf3")  # Use a tuple has to be hashable and a list does not work...
action = agent(percept_sequence)
print(action)
