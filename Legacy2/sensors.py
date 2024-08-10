"""Module providing the Sensors class."""

from dataclasses import dataclass

from chess import Board
from environment import Environment


@dataclass
class Sensors:
    """Class representing sensors, through which an agent can perceive its environment."""

    def __call__(self, environment: Environment) -> Board:
        pass
