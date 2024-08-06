"""Module providing the ChessTreeSensors class."""

from dataclasses import dataclass

from chess_tree_environment import ChessTreeEnvironment
from chess_tree_percept import ChessTreePercept
from sensors import Sensors

@dataclass
class ChessTreeSensors(Sensors):
    """Class representing chess tree sensors."""

    def __call__(self, environment: ChessTreeEnvironment) -> ChessTreePercept:
        assert 0
