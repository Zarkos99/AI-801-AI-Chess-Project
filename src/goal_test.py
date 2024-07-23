"""Module providing the GoalTest class."""

from dataclasses import dataclass

@dataclass
class GoalTest:
    """Class representing a goal test, which determines whether a given state is a goal state."""

    def __call__(self, s) -> bool:
        pass
