"""Module providing the ChessTreeAction class."""

from dataclasses import dataclass

from action import Action

@dataclass
class ChessTreeAction(Action):
    """Class representing a chess tree action."""
