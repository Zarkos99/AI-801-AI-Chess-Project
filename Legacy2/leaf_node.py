"""Module providing the LeafNode class."""

from dataclasses import dataclass

from node import Node

@dataclass
class LeafNode(Node):
    """Class representing a leaf node, which is a node with no children in the tree."""
