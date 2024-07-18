"""Module providing the Actuators class."""

from dataclasses import dataclass

from action import Action
from environment import Environment

@dataclass
class Actuators:
    """Class representing actuators, through which an agent can act upon its environment."""

    def __call__(self, action: Action, environment: Environment):
        pass
