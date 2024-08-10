"""Module providing the Percept class."""

from dataclasses import dataclass

from state import State

@dataclass
class Percept:
    """Class representing a percept, which is an agent's perceptual inputs at any given time."""

    state: State = None
