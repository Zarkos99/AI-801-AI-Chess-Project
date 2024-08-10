"""Module providing the Sensors class."""

from dataclasses import dataclass

from environment import Environment
from percept import Percept
from state import State

@dataclass
class Sensors:
    """Class representing sensors, through which an agent can perceive its environment."""

    def __call__(self, environment: Environment) -> Percept:
        state = State(environment.gamenode.board())
        percept = Percept(state=state)

        return percept
