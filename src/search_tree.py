"""Module providing the SearchTree class."""

from dataclasses import dataclass

from generate import generate

@dataclass
class SearchTree:
    """Class representing a search tree, which is formed by the possible action sequences starting\
       at the initial state (the root)."""

    def expand(self, problem, s) -> list:
        """Function for considering taking various actions, which is done by generating a new set\
           of states from the current state."""
        return generate(problem, s)
