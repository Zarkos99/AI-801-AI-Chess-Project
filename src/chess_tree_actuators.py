"""Module providing the ChessTreeActuators class."""

from dataclasses import dataclass

from actuators import Actuators
from chess_tree_action import ChessTreeAction
from chess_tree_environment import ChessTreeEnvironment

@dataclass
class ChessTreeActuators(Actuators):
    """Class representing chess tree actuators."""

    def __call__(self, action: ChessTreeAction, environment: ChessTreeEnvironment):
        assert 0
