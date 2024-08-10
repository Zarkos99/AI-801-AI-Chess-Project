"""Module providing the ChessTreePercept class."""

from dataclasses import dataclass

from chess_tree_state import ChessTreeState
from percept import Percept

@dataclass
class ChessTreePercept(Percept):
    """Class representing a chess tree percept."""

    state: ChessTreeState = None
