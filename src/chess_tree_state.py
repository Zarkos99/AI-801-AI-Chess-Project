"""Module providing the ChessTreeState class."""

from dataclasses import dataclass

from state import State

@dataclass
class ChessTreeState(State):
    """Class representing a chess tree state."""
