"""Module providing the ChessPuzzlePercept class."""

from dataclasses import dataclass

from chess_puzzle_state import ChessPuzzleState
from chess_tree_environment import ChessTreeEnvironment
from percept import Percept

@dataclass
class ChessPuzzlePercept(Percept):
    """Class representing a chess puzzle percept."""

    knowledge: ChessTreeEnvironment = None
    state: ChessPuzzleState = None
    time_remaining: bool = False
