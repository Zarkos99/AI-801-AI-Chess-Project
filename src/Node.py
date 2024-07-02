
from Action import Action
from Actions import Actions
from PathCost import PathCost
from Result import Result
from State import State
from Step_Cost import step_cost

class Node:
    def __init__(self, par_state: State, 
                 par_parent = None,
                 par_action: Action = None,
                 par_children = [],
                 par_path_cost: PathCost = 0.0):
        self.state = par_state
        self.parent = par_parent
        self.action = par_action
        self.children = par_children
        self.path_cost = par_path_cost

def Expand(par_node: Node):
    actions = Actions(par_node.state)
    
    for action in actions:
        result = Result(par_node.state, action)

        if not result.check:
            child = ChildNode(par_node, action)
            par_node.children.append(child)

def ChildNode(par_parent: Node, par_action: Action):
    state = Result(par_parent.state, par_action)
    path_cost = par_parent.path_cost + step_cost(par_parent.state, par_action)
    
    return Node(state, par_parent, par_action, None, path_cost)

def Solution(par_node: Node):
    solution = []
    node = par_node
    
    while (not (node.parent is None)):
        solution.append(node.action)
        node = node.parent
    
    solution = reversed(solution)
    
    return solution
