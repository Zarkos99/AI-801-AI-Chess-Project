"""Module providing the TransitionModel class."""

from dataclasses import dataclass

from action import Action
from state import State

@dataclass
class TransitionModel:
    """Class representing a transition model, which is a description of what each action does."""

    # Returns the state that results from doing action a in state s
    def __call__(self, s: State, a: Action) -> State:
        result = s.copy()
        result.push(a)

        return result
