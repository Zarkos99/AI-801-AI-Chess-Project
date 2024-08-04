"""Module providing the Path class."""

from dataclasses import dataclass

from state import State

@dataclass
class Path(list[State]):
    """Class representing a path, which is a sequence of states in the state space connected by a\
       sequence of actions."""
