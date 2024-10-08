"""Module providing the Node class."""

from dataclasses import dataclass
from typing import Self

from action import Action
from state import State

@dataclass
class Node:
    """Class representing a node, which corresponds to states in the state space of the problem."""

    state: State = None
    parent: Self = None
    action: Action = None
    path_cost: float = 0.0
