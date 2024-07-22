"""Module providing the PerformanceMeasure class."""

from dataclasses import dataclass

from environment import Environment

@dataclass
class PerformanceMeasure:
    """Class representing a performance measure, which evaluates the desirability of any given\
       sequence of environment states"""

    def __call__(self, environment_state_sequence: list[Environment]) -> bool:
        pass
