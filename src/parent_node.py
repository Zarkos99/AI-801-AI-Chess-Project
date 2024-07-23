"""Module providing the ParentNode class."""

from dataclasses import dataclass

from node import Node

@dataclass
class ParentNode(Node):
    """Class representing a parent node, which is a node from which branches leading to child\
       nodes are added."""
