"""Module providing the Actions class."""

from dataclasses import dataclass
from typing import Generator

from action import Action
from state import State

@dataclass
class Actions:
    """Class representing a description of the possible actions available to the agent."""

    # Given a particular state s, Actions(s) returns the set of actions that can be executed in s.
    def __call__(self, s: State) -> Generator[Action, None, None]:
        return s.generate_legal_moves
