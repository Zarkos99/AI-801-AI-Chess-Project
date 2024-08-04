"""Module providing the Strategy class."""

from dataclasses import dataclass

@dataclass
class Strategy:
    """Class representing a strategy, which specifies player MAX's move in the initial state, then\
       MAX's moves in the states resulting from every possible response by player MIN, then MAX's\
       moves in the states resulting from every possible response by MIN to those moves, and so\
       on. This is exactly analogous to the AND-OR search algorithm with MAX playing the role of\
       OR and MIN equivalent to AND."""
