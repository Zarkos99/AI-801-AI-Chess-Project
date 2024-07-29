"""Module providing the AgentProgram class."""

from dataclasses import dataclass

from chess import Board
from action import Action


@dataclass
class AgentProgram:
    """Class representing an agent program, which implements the agent function."""

    def __call__(self, percept: Board) -> Action:
        pass
