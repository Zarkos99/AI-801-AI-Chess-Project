"""Module providing the ChessPuzzle class."""

from dataclasses import dataclass, field

@dataclass
class ChessPuzzle:
    """Class representing a chess puzzle, in the format specified by the source (chess.com)."""
    title: str
    url: str
    publish_time: int
    fen: str
    pgn: str
    image: str
    comments: str = field(default_factory=str)
