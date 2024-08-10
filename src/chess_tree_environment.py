"""Module providing the ChessTreeEnvironment class."""

from dataclasses import dataclass

from environment import Environment

@dataclass
class ChessTreeEnvironment(Environment):
    """Class representing a chess tree environment."""
