"""Module providing the Sensors class."""

from dataclasses import dataclass

from environment import Environment
from percept import Percept

@dataclass
class Sensors:
    """Class representing sensors, through which an agent can perceive its environment."""

    def __call__(self, environment: Environment) -> Percept:
        pass
