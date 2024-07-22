
from numpy import inf

from Action import Action
from Actions import Actions
from PathCost import PathCost
from Result import Result
from State import State
from Step_Cost import step_cost


class Node:
    def __init__(self, par_state: State,
                 par_parent=None,
                 par_action: Action = None):
        self.state = par_state
        self.parent = par_parent
        self.action = par_action
        self.children = []
        self.path_cost = PathCost(par_state)

    # Finds the child with the lowest path cost
    def MinElement(self):
        assert (len(self.children) > 0)
        min_element = None
        min_path_cost = inf

        for child in self.children:
            path_cost = float(child.path_cost)
            if path_cost < min_path_cost:
                min_element = child
                min_path_cost = float(child.path_cost)

        return min_element


def Expand(par_node: Node):
    actions = Actions(par_node.state)

    for action in actions:
        result = Result(par_node.state, action)

        if not result.check:
            child = ChildNode(par_node, action)
            par_node.children.append(child)

    par_node.path_cost.expanded = True

    UpdateTree(par_node)


def ChildNode(par_parent: Node, par_action: Action):
    result = Result(par_parent.state, par_action)

    return Node(result, par_parent, par_action)


def Solution(par_node: Node):
    solution = []
    node = par_node

    while (not (node.parent is None)):
        solution.append(node.action)
        node = node.parent

    solution = reversed(solution)

    return solution


def UpdateTree(par_node: Node):
    node = par_node

    while not (node is None):
        # assert (node.path_cost.expanded) defaults to false?
        if len(node.children) > 0:
            min_child = node.MinElement()
            if min_child is not None:
                node.path_cost.min_child_cost = float(min_child.path_cost)

            if node.path_cost.min_child_cost == 0.0:
                node.children.clear()

        node.path_cost.child_count = len(node.children)

        node = node.parent
