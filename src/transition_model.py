"""Module providing the TransitionModel class."""

from dataclasses import dataclass

from action import Action

@dataclass
class TransitionModel:
    """Class representing a transition model, which is a description of what each action does."""

    # Returns the state that results from doing action a in state s
    def __call__(self, s, a: Action):
        pass
