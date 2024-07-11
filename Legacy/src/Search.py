
from numpy import isinf
from time import time

from Action import Action
from Node import Node, Expand
from State import State

def Search(par_initial_state: State, par_seconds = 5.0):
    root = Node(par_initial_state)
    seconds_elapsed = 0.0
    start = time()
    
    while seconds_elapsed < par_seconds:
        root_expanded = root.path_cost.expanded
        root_cost = float(root.path_cost)
        is_done = root_expanded and (isinf(root_cost) or root_cost == 0.0)

        if is_done: break
        
        node = root

        while node.path_cost.expanded:
            node = node.MinElement()
        
        Expand(node)
        
        seconds_elapsed = time() - start
    
    if len(root.children) == 0:
        return Action()
        
    result = root.MinElement()

    return result.action
