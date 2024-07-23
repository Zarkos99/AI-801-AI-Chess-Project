"""Module providing the Actions class."""

from dataclasses import dataclass

from action import Action

@dataclass
class Actions:
    """Class representing a description of the possible actions available to the agent."""

    # Given a particular state s, Actions(s) returns the set of actions that can be executed in s.
    def __call__(self, s) -> list[Action]:
        pass
