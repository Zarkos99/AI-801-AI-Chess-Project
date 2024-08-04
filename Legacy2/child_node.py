"""Module providing the ChildNode class."""

from dataclasses import dataclass

from action import Action
from node import Node
from parent_node import ParentNode
from problem import Problem

@dataclass
class ChildNode(Node):
    """Class representing a child node, which is a node lead to by a branch from the parent node.\
       """

    def __init__(self, problem: Problem, parent: ParentNode, action: Action):
        state = problem.result(parent.state, action)
        path_cost = parent.path_cost + problem.step_cost(parent.state, action)

        super().__init__(state, parent, action, path_cost)
