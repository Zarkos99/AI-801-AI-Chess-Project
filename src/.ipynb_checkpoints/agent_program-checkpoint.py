"""Module providing the AgentProgram class."""

from dataclasses import dataclass

from action import Action
from percept import Percept

@dataclass
class AgentProgram:
    """Class representing an agent program, which implements the agent function."""

    def __call__(self, percept: Percept) -> Action:
        print(percept)
