"""Module providing the AgentFunction class."""

from dataclasses import dataclass

from chess import Board
from action import Action


@dataclass
class AgentFunction:
    """Class representing an agent function, which is an abstract mathematical description of an\
       agent's behavior that maps any given percept sequence to an action."""

    def __init_subclass__(cls):
        cls.partial_table = dict[Board, Action]()

        # Convert puzzles to percept_sequence-action pairs and add to partial table
        # ...

    def __call__(self, percept_sequence: Board) -> Action:
        return self.partial_table[percept_sequence]
