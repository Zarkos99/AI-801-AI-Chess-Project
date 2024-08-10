"""Module providing the ChessPuzzleAction class."""

from dataclasses import dataclass

from chess import Move

from action import Action

@dataclass
class ChessPuzzleAction(Action):
    """Class representing a chess puzzle action."""

    thinking = True
    move: Move = None
