"""Module providing the Action class."""

from dataclasses import dataclass

from chess import Move

@dataclass
class Action:
    """Class representing an action, which is an act that can be executed in a particular state."""

    move: Move

    def __hash__(self) -> int:
        return hash(self.move)
