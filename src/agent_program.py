"""Module providing the AgentProgram class."""

from dataclasses import dataclass
#from random import uniform
from math import ceil
from time import time
from typing import ClassVar, Self

#import chess

from action import Action
from game import Game
from percept import Percept
from state import State

DEBUG = False
TIME_LIMIT = 3.0

#@dataclass
#class Node:
#    def __init__(self, state: State = None, parent: Self = None, action: Action = None, expanded: bool = False):
#        self.state: State = state
#        self.parent: Self = parent
#        self.action: Action = action
#        self.expanded: bool = expanded
#
#@dataclass
#class AlphaBetaNode(Node):
#    def __init__(self, state: State = None, parent: Self = None, action: Action = None, expanded: bool = False, value: float = 0.0, is_max_node: bool = False, alpha: float = 0.0, beta: float = float('inf')):
#        super().__init__(state, parent, action, expanded)
#        self.value: float = value
#        self.is_max_node: bool = is_max_node
#        self.alpha: float = alpha
#        self.beta: float = beta
#        self.children: dict[Action, Self] = {}
#        AgentProgram.leaf_nodes_alive += 1
#        
#    def __del__(self):
#        if self.expanded:
#            assert AgentProgram.parent_nodes_alive
#            AgentProgram.parent_nodes_alive -= 1
#        else:
#            assert AgentProgram.leaf_nodes_alive
#            AgentProgram.leaf_nodes_alive -= 1

nodes_created = 0
nodes_explored = 0
nodes_deleted = 0

@dataclass
class AgentProgram:
    """Class representing an agent program, which implements the agent function."""

    #def __call__(self, percept: Percept) -> Action:
    #    self.__game = Game(percept.state)
    #    self.__player = percept.state.board.turn
    #    self.__root = AlphaBetaNode(state=percept.state,
    #                                is_max_node=True,
    #                                value=self.__eval(percept.state),
    #                                alpha=0.0,
    #                                beta=float('inf'))
    #    start_time = time()
    #
    #    while time() - start_time < TIME_LIMIT:
    #        if self.__root.value == float('inf'):
    #            action = max(self.__root.children, key=lambda p: self.__root.children[p].value)
    #            return action
    #
    #        if self.__root.value == 0:
    #            return None
    #        
    #        node = self.__next()
    #        self.__expand(node)
    #        self.__prune(node)
    #        
    #        if DEBUG:
    #            print("Parents alive: ", AgentProgram.parent_nodes_alive,
    #                  ", Leaves alive: ", AgentProgram.leaf_nodes_alive)
    #    
    #    action = max(self.__root.children, key=lambda p: self.__root.children[p].value)
    #    return action
    
    def __call__(self, percept: Percept) -> Action:
        game = Game(percept.state)
        terminal_test = game.terminal_test
        utility = game.utility
        player = percept.state.board.turn
        actions = game.actions
        result = game.result
        
        ALPHA_0 = 0
        BETA_0 = float('inf')

        @dataclass
        class Node:
            def __init__(self, state: State, alpha: float, beta: float):
                self.state: State = state
                self.value: float = None
                self.alpha: float = alpha
                self.beta: float = beta

                if terminal_test(state):
                    self.value = utility(state, player)
                
                global nodes_created
                global nodes_deleted
                global nodes_explored
                
                nodes_created = nodes_created + 1
                #print("NODES - Created: ", nodes_created, ", Deleted: ", nodes_deleted, ", Alive: ", nodes_created - nodes_deleted, ", Explored: ", nodes_explored)
                
            def __del__(self):
                global nodes_created
                global nodes_deleted
                global nodes_explored
                
                nodes_deleted = nodes_deleted + 1
                #print("NODES - Created: ", nodes_created, ", Deleted: ", nodes_deleted, ", Alive: ", nodes_created - nodes_deleted, ", Explored: ", nodes_explored)

        class MaxNode(Node):
            def __init__(self, state: State, alpha: float, beta: float):
                super().__init__(state, alpha, beta)
                self.parent: MinNode = None
                self.children: list[MinNode] = []
                
                if self.value is None:
                    for a in actions(state):
                        sp = result(state, a)
                        child = MinNode(sp, alpha, beta)
                        child.parent = self
                        self.children.append(child)
                    
                    sorted_children = sorted(self.children, key=lambda c: c.order, reverse=True)

                    self.children.clear()
                    percent = 0.2 if state.board.move_stack else 0.4
                    child_count = int(ceil(len(sorted_children) * percent))
                    self.children = sorted_children[0:child_count]

                    max_child = max(self.children, key=lambda c: c.order)
                    assert max_child.order is not None
                    self.order: float = max_child.order
                else:
                    assert self.value is not None
                    self.order: float = self.value

        class MinNode(Node):
            def __init__(self, state: State, alpha: float, beta: float):
                super().__init__(state, alpha, beta)
                self.parent: MaxNode = None
                self.children: list[MaxNode] = []
                self.explored: bool = False

                if self.value is None:
                    self.order: float = 1.0 / state.board.legal_moves.count()
                else:
                    self.order: float = self.value

        #class ABNode:
        #    def __init__(self, state: State, max_node: bool, alpha: float, beta: float):
        #        self.state: State = state
        #        self.parent: Self = None
        #        self.is_max_node: bool = max_node
        #        self.value: float = None
        #        self.alpha: float = alpha
        #        self.beta: float = beta
        #        self.explored: bool = False
        #        self.children: list[Self] = []
        #        self.order: float = None
        #
        #        if terminal_test(state):
        #            self.value = utility(state, player)
        #            self.explored = True
        #        else:
        #            legal_moves = state.board.legal_moves.count()
        #            self.order: float = 1.0 / legal_moves if legal_moves else BETA_0
        #
        #    def evaluate(self) -> float:
        #        if self.value:
        #            return self.value
        #        
        #        if self.explored:
        #            if self.is_max_node:
        #                return max()
        #            return self.children
            #def evaluate(self) -> float:
            #    if self.value:
            #        return self.value
            #    
            #    move_eval = self.evaluate_moves()
            #    piece_eval = self.evaluate_pieces()
            #
            #    return move_eval * piece_eval
            #    
            #def evaluate_moves(self) -> float:
            #    s = self.state
            #    s_parent = self.parent.state if self.parent else None
            #    move_count = s.board.legal_moves.count()
            #    parent_move_count = s_parent.board.legal_moves.count() if s_parent else move_count
            #
            #    move_num = 0
            #    move_den = 0
            #
            #    if s.board.turn == player:
            #        move_num = move_count
            #        move_den = parent_move_count
            #    else:
            #        move_num = parent_move_count
            #        move_den = move_count
            #    
            #    move_ratio = float('inf') if move_den == 0 else move_num / move_den
            #    
            #    return move_ratio
            #
            #def evaluate_pieces(self) -> float:
            #    s = self.state
            #    def pieces_value(color: bool) -> float:
            #        pawns = len(s.board.pieces(chess.PAWN, color))
            #        knights = len(s.board.pieces(chess.KNIGHT, color))
            #        bishops = len(s.board.pieces(chess.BISHOP, color))
            #        rooks = len(s.board.pieces(chess.ROOK, color))
            #        queens = len(s.board.pieces(chess.QUEEN, color))
            #        value: float = pawns + knights*2.0 + bishops*3.0 + rooks*5.0 + queens*9.0
            #
            #        return value
            #
            #    w_pieces = pieces_value(chess.WHITE)
            #    b_pieces = pieces_value(chess.BLACK)
            #
            #    pieces_num = 0
            #    pieces_den = 0
            #
            #    if player == chess.WHITE:
            #        pieces_num = w_pieces
            #        pieces_den = b_pieces
            #    else:
            #        pieces_num = b_pieces
            #        pieces_den = w_pieces
            #    
            #    pieces_ratio = float('inf') if pieces_den == 0 else pieces_num / pieces_den
            #
            #    return pieces_ratio

        #def area_limited_search(root: ABNode, depth_limit: int, depth: int, width_percent: float) -> ABNode:
        #    return area_limited_search_rec(root, depth_limit, depth, width_percent)
        #
        #def area_limited_search_rec(node: ABNode, depth_limit: int, depth: int, width_percent: float) -> ABNode:
        #    if not node.explored:
        #        return node
        #    
        #    if depth == depth_limit:
        #        return None
        #
        #    sorted_children = sorted(node.children, key=lambda c: c.order if c.value is None else c.value, reverse=node.is_max_node)
        #    child_count = len(sorted_children)
        #    #width = int(round(child_count * width_percent / (depth + 1))) if node.is_max_node else child_count
        #    width = child_count
        #
        #    for i in range(width):
        #        child = area_limited_search_rec(sorted_children[i], depth_limit, depth + 1, width_percent)
        #
        #        if child:
        #            return child
        #    
        #    return None

        def expand(node: MinNode, frontier: list[MinNode]):
            for a in actions(node.state):
                sp: State = result(node.state, a)
                child: MaxNode = MaxNode(sp, node.alpha, node.beta)
                child.parent = node
                node.children.append(child)
                
                for c in child.children:
                    frontier.insert(0, c)

            node.explored = True
            
            global nodes_created
            global nodes_deleted
            global nodes_explored
            
            nodes_explored += 1
            #print("NODES - Created: ", nodes_created, ", Deleted: ", nodes_deleted, ", Alive: ", nodes_created - nodes_deleted, ", Explored: ", nodes_explored)
  
        #def iterative_expanding_search(root: ABNode) -> ABNode:
        #    depth_limit = 0
        #    width_percent = 0.33
        #
        #    while True:
        #        node = area_limited_search(root, depth_limit, 0, width_percent)
        #
        #        if node:
        #            return node
        #
        #        depth_limit += 1

        #def max_node(state: State, alpha: float, beta: float) -> ABNode:
        #    return ABNode(state, True, alpha, beta)
        #
        #def min_node(state: State, alpha: float, beta: float) -> ABNode:
        #    return ABNode(state, False, alpha, beta)

        def next_node(root: MaxNode) -> MinNode:
            child = max(root.children, key=lambda c: c.order)
            
            while child.explored:
                node = min(child.children, key=lambda c: c.order)
                child = max(node.children, key=lambda c: c.order)

            return child

        def prune(node: MinNode):
            while node:
                if not node.children:
                    node.value = BETA_0
                    node.order = node.value
                elif len(node.children) == 1 and node.children[0].value is not None:
                    node.value = node.children[0].value
                    node.order = node.value
                else:
                    v = BETA_0
                    set_value = True
                        
                    for child in node.children:
                        if child.value is not None:
                            v = min(v, child.value)
                            
                            if v <= node.alpha:
                                set_value = True
                                break
                            
                            node.beta = min(node.beta, v)
                        else:
                            set_value = False
                            
                    if set_value:
                        min_child = min(node.children, key=lambda c: c.value if c.value else BETA_0)
                        
                        node.children.clear()
                        node.children.append(min_child)
                        node.value = min_child.value
                        assert node.value is not None
                        node.order = node.value
                    else:
                        min_child = min(node.children, key=lambda c: c.order)
                        node.order = min_child.order
                        
                parent = node.parent
                node = None
                
                if parent:
                    v = ALPHA_0
                    set_value = True

                    for child in parent.children:
                        if child.value is not None:
                            v = max(v, child.value)
                            
                            if v >= parent.beta:
                                set_value = True
                                break
                            
                            parent.alpha = max(parent.alpha, v)
                        else:
                            set_value = False
                            
                    if set_value:
                        max_child = max(parent.children, key=lambda c: c.value if c.value else ALPHA_0)
                        
                        parent.children.clear()
                        parent.children.append(max_child)
                        parent.value = max_child.value
                        parent.order = parent.value
                    else:
                        max_child = max(parent.children, key=lambda c: c.order)
                        parent.order = max_child.order
                
                    node = parent.parent
                
        root: MaxNode = MaxNode(percept.state, ALPHA_0, BETA_0)
        frontier: list[MinNode] = []
        
        for child in root.children:
            frontier.insert(0, child)
            
        start_time: float = time()
        elapsed_time = 0.0
        depth = 0
        
        while elapsed_time < TIME_LIMIT and root.value != BETA_0:
            if root.value == ALPHA_0:
                return None

            #node = next_node(root)
            node = frontier.pop()
            expand(node, frontier)
            prune(node)

            v1 = None
            v2 = None
            v3 = None

            sorted_children = sorted(root.children, key=lambda c: c.order, reverse=True)
            for i in range(len(sorted_children)):
                if sorted_children[i].state.board.peek().uci() == "d1g4":
                    v1 = i / len(sorted_children)
                    sorted_children2 = sorted(sorted_children[i].children, key=lambda c: c.order)
                    for j in range(len(sorted_children2)):
                        if sorted_children2[j].state.board.peek().uci() == "g7g6":
                            v2 = j / len(sorted_children2)
                            sorted_children3 = sorted(sorted_children2[j].children, key=lambda c: c.order, reverse=True)
                            for k in range(len(sorted_children3)):
                                if sorted_children3[k].state.board.peek().uci() == "g4d4":
                                    v3 = k / len(sorted_children3)
                                    break
                            break
                    break
                
            print(v1, v2, v3)

            #elapsed_time = time() - start_time
        
        max_child: MinNode = None
        
        if root.value is None:
            max_child = max(root.children, key=lambda c: c.order)
        else:
            max_child = max(root.children, key=lambda c: c.value if c.value else ALPHA_0)
            
        action = Action(max_child.state.board.peek())

        return action

    #def __child_node(self, parent: AlphaBetaNode, action: Action) -> AlphaBetaNode:
    #    state = self.__game.result(parent.state, action)
    #    value = self.__eval(state, parent.state)
    #    is_max_node = not parent.is_max_node
    #    alpha = parent.alpha
    #    beta = parent.beta
    #    
    #    child = AlphaBetaNode(state=state,
    #                          parent=parent,
    #                          action=action,
    #                          value=value,
    #                          is_max_node=is_max_node,
    #                          alpha=alpha,
    #                          beta=beta)
    #    parent.children[action] = child
    #
    #    return child

    #def __eval(self, s: State, s_parent: State = None) -> float:
    #    if self.__game.terminal_test(s):
    #        return self.__game.utility(s, self.__player)
    #    
    #    def pieces_value(color: bool) -> float:
    #        pawns = len(s.board.pieces(chess.PAWN, color))
    #        knights = len(s.board.pieces(chess.KNIGHT, color))
    #        bishops = len(s.board.pieces(chess.BISHOP, color))
    #        rooks = len(s.board.pieces(chess.ROOK, color))
    #        queens = len(s.board.pieces(chess.QUEEN, color))
    #        value: float = pawns + knights*2.0 + bishops*3.0 + rooks*5.0 + queens*9.0
    #        
    #        return value
    #    
    #    w_pieces = pieces_value(chess.WHITE)
    #    b_pieces = pieces_value(chess.BLACK)
    #
    #    move_count = s.board.legal_moves.count()
    #    parent_move_count = s_parent.board.legal_moves.count() if s_parent else move_count
    #    
    #    move_num = 0
    #    move_den = 0
    #
    #    if s.board.turn == self.__player:
    #        move_num = move_count
    #        move_den = parent_move_count
    #    else:
    #        move_num = parent_move_count
    #        move_den = move_count
    #        
    #    pieces_num = 0
    #    pieces_den = 0
    #    
    #    if self.__player == chess.WHITE:
    #        pieces_num = w_pieces
    #        pieces_den = b_pieces
    #    else:
    #        pieces_num = b_pieces
    #        pieces_den = w_pieces
    #    
    #    move_ratio = float('inf') if move_den == 0 else move_num / move_den
    #    pieces_ratio = float('inf') if pieces_den == 0 else pieces_num / pieces_den
    #
    #    eval_ = move_ratio * pieces_ratio
    #    return eval_

    #def __expand(self, node: AlphaBetaNode):
    #    s = node.state
    #    is_max_node = node.is_max_node
    #    node.value = 0 if is_max_node else float('inf')
    #
    #    for a in self.__game.actions(s):
    #        self.__child_node(node, a)
    #
    #    node.expanded = True
    #    
    #    assert AgentProgram.leaf_nodes_alive
    #    AgentProgram.leaf_nodes_alive -= 1
    #    AgentProgram.parent_nodes_alive += 1

    #def __next(self) -> AlphaBetaNode:
    #    node = self.__root
    #
    #    while node.expanded:
    #        is_max_node = node.is_max_node
    #        actions = sorted(node.children, key=lambda p: node.children[p].value, reverse=is_max_node)
    #        a = len(actions) - 1
    #        rand = int(round(abs(uniform(-a, a))))
    #        action = actions[rand]
    #        node = node.children[action]
    #
    #    return node

    #def __prune(self, node: AlphaBetaNode):
    #    while node:
    #        if node.parent:
    #            node.alpha = max(node.alpha, node.parent.alpha)
    #            node.beta = min(node.beta, node.parent.beta)
    #        
    #        is_max_node = node.is_max_node
    #        node.value = 0 if is_max_node else float('inf')
    #        all_children_expanded = True
    #
    #        for a, child in node.children.items():
    #            if not child.expanded:
    #                all_children_expanded = False
    #                break
    #            
    #        if is_max_node:
    #            action = max(node.children, key=lambda a: node.children[a].value)
    #            node.value = node.children[action].value
    #            node.alpha = max(node.alpha, node.value)
    #        else:
    #            action = min(node.children, key=lambda a: node.children[a].value)
    #            node.value = node.children[action].value
    #            node.beta = min(node.beta, node.value)
    #        
    #        if all_children_expanded:
    #            children: dict[Action, AlphaBetaNode] = {}
    #            
    #            for a, child in node.children.items():
    #                if child.value == node.value:
    #                    children[a] = child
    #            
    #            node.children.clear()
    #            node.children = children
    #
    #        node = node.parent

    #__game: Game = None
    #__player: bool = None
    #__root: AlphaBetaNode = None

    #leaf_nodes_alive: ClassVar[int] = 0
    #parent_nodes_alive: ClassVar[int] = 0
