"""Module providing the ChessPuzzleState class."""

from dataclasses import dataclass

from chess import Board

from state import State

@dataclass
class ChessPuzzleState(State):
    """Class representing a chess puzzle state."""

    board: Board = None
