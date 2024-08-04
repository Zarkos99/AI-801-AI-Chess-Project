"""Module providing the StepCost class."""

from dataclasses import dataclass

from action import Action

@dataclass
class StepCost:
    """Class representing a step cost function, which is the path cost between a state and its\
       successor."""

    def __call__(self, s, a: Action, sp) -> float:
        pass
