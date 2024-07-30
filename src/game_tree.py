"""Module providing the GameTree class."""

from dataclasses import dataclass, field

from actions import Actions
from state import State
from transition_model import TransitionModel

@dataclass
class GameTree:
    """Class representing a game tree, which is a tree where the nodes are the game states and the\
       edges are the moves."""

    initial_state: State = None
    actions: Actions = field(default_factory=Actions)
    result: TransitionModel = field(default_factory=TransitionModel)
