"""Module providing the AgentFunction class."""

from dataclasses import dataclass

from action import Action
from percept_sequence import PerceptSequence

@dataclass
class AgentFunction:
    """Class representing an agent function, which is an abstract mathematical description of an\
       agent's behavior that maps any given percept sequence to an action."""

    def __init__(self):
        self.partial_table = dict[PerceptSequence, Action]()

        # Convert puzzles to percept_sequence-action pairs and add to partial table
        # ...

    def __call__(self, percept_sequence: PerceptSequence) -> Action:
        return self.partial_table[percept_sequence]
