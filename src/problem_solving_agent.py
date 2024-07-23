"""Module providing the ProblemSolvingAgent class."""

from dataclasses import dataclass

@dataclass
class ProblemSolvingAgent:
    """Class representing a problem-solving agent, which is one kind of goal-based agent that uses\
       atomic representations (that is, states of the world are considered as wholes, with no\
       internal structure visible to the problem-solving algorithms)."""
