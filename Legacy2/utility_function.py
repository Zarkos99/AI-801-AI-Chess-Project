"""Module providing the UtilityFunction class."""

from dataclasses import dataclass

from player import Player
from state import State

@dataclass
class UtilityFunction:
    """Class representing a utility function, also called an objective function or payoff\
       function, which defines the final numeric value for a game that ends in terminal state s\
       for player p."""

    def __call__(self, s: State, p: Player) -> float:
        pass
