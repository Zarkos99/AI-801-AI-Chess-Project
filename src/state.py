"""Module providing the State class."""

from dataclasses import dataclass

from chess import Board

@dataclass
class State:
    """Class representing a state, which is a representation of knowledge."""

    board: Board
