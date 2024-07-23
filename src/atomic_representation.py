"""Module providing the AtomicRepresentation class."""

from dataclasses import dataclass

@dataclass
class AtomicRepresentation:
    """Class representing an atomic representation, which is a representation of the environment\
       in which each state is indivisible (i.e. it has no internal structure)."""
