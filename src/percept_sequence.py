"""Module providing the PerceptSequence class."""

from dataclasses import dataclass, field

from percept import Percept

@dataclass
class PerceptSequence:
    """Class representing an agent's percept sequence, which is the complete history of everything\
       the agent has ever perceived."""

    history: list[Percept] = field(default_factory=list[Percept])
