"""Module providing the PathCost class."""

from dataclasses import dataclass

@dataclass
class PathCost:
    """Class representing a path cost function, which assigns a numeric cost to each path."""

    def __call__(self, path) -> float:
        pass
