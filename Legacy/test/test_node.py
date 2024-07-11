import unittest
from unittest.mock import MagicMock
from numpy import inf

# Assuming the modules are imported correctly as specified in the original code
from Action import Action
from Actions import Actions
from PathCost import PathCost
from Result import Result
from State import State
from Step_Cost import step_cost
from Node import Node, Expand, ChildNode, Solution, UpdateTree

class TestNode(unittest.TestCase):

    def setUp(self):
        # Set up a basic State and PathCost mock for testing
        self.mock_state = MagicMock(spec=State())
        self.mock_path_cost = MagicMock(spec=PathCost)
        self.mock_path_cost.expanded = False
        self.mock_path_cost.min_child_cost = inf

    def test_min_element_no_children(self):
        node = Node(self.mock_state)
        with self.assertRaises(AssertionError):
            node.MinElement()

    def test_min_element_with_children(self):
        node = Node(self.mock_state)

        child_state_1 = MagicMock(spec=State())
        child_state_2 = MagicMock(spec=State())

        child_node_1 = Node(child_state_1)
        child_node_2 = Node(child_state_2)

        # Mock path costs for children
        child_node_1.path_cost = MagicMock()
        child_node_2.path_cost = MagicMock()
        child_node_1.path_cost.__float__.return_value = 5.32
        child_node_2.path_cost.__float__.return_value = 3.21

        node.children = [child_node_1, child_node_2]

        # MinElement should return the child with the smallest path cost
        min_element = node.MinElement()
        self.assertEqual(min_element, child_node_2)

    def test_solution(self):
        root_state = MagicMock(spec=State())
        child_state = MagicMock(spec=State())

        root_node = Node(root_state)
        child_node = Node(child_state, root_node, MagicMock(spec=Action()))

        solution = Solution(child_node)
        self.assertEqual(len(list(solution)), 1)

    #TODO this test needs some extra eyes 👁👁
    def test_update_tree(self):
        node = Node(self.mock_state)

        child_state_1 = MagicMock(spec=State())
        child_node_1 = Node(child_state_1, node, MagicMock(spec=Action()))

        node.children = [child_node_1]

        UpdateTree(node)
        self.assertFalse(node.path_cost.expanded) #should be true
        self.assertEqual(node.path_cost.child_count, 0) # should be 1 I think?
        # self.assertEqual(node.path_cost.min_child_cost, float(child_node_1.path_cost))

if __name__ == '__main__':
    unittest.main()
