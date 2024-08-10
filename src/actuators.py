"""Module providing the Actuators class."""

from dataclasses import dataclass

from action import Action
from environment import Environment

@dataclass
class Actuators:
    """Class representing actuators, through which an agent can act upon its environment."""

    def __call__(self, action: Action, environment: Environment):
        assert action.move == environment.gamenode.next().move

        environment.gamenode = environment.gamenode.next()

        if environment.gamenode.next():
            environment.gamenode = environment.gamenode.next()

        environment.display = True
