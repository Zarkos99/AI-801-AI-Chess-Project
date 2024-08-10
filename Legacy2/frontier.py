"""Module providing the Frontier class."""

from dataclasses import dataclass

@dataclass
class Frontier:
    """Class representing a frontier, which is the set of all leaf nodes available for expansion\
       at any given point."""

OpenList = Frontier
