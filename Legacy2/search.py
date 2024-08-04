"""Module providing the Search class."""

from dataclasses import dataclass

from problem import Problem
from solution import Solution

@dataclass
class Search:
    """Class representing a search, which is the process of looking for a sequence of actions that\
       reaches the goal."""

    @dataclass
    class Tree:
        """Class representing a search tree, which is a tree that is superimposed on the full game\
           tree, and examines enough nodes to allow a player to determine what move to make."""

    def __call__(self, problem: Problem) -> Solution:
        pass
