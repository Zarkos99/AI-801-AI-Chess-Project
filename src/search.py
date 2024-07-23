"""Module providing the search function."""

from problem import Problem
from solution import Solution

def search(problem: Problem) -> Solution:
    """Function that looks for a sequence of actions that reaches the goal."""

    if problem is None:
        return Solution()

    return None
