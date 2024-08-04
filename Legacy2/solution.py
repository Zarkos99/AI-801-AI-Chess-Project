"""Module providing the Solution class."""

from dataclasses import dataclass

from action import Action

@dataclass
class Solution(list[Action]):
    """Class representing a solution, which is an action sequence returned by a search algorithm.\
       """
