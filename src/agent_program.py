"""Module providing the AgentProgram class."""

from dataclasses import dataclass
from random import uniform
from time import time
from typing import ClassVar, Self

import chess

from action import Action
from game import Game
from percept import Percept
from state import State

DEBUG = False
TIME_LIMIT = 3.0

@dataclass
class Node:
    def __init__(self, state: State = None, parent: Self = None, action: Action = None, expanded: bool = False):
        self.state: State = state
        self.parent: Self = parent
        self.action: Action = action
        self.expanded: bool = expanded

@dataclass
class AlphaBetaNode(Node):
    def __init__(self, state: State = None, parent: Self = None, action: Action = None, expanded: bool = False, value: float = 0.0, is_max_node: bool = False, alpha: float = 0.0, beta: float = float('inf')):
        super().__init__(state, parent, action, expanded)
        self.value: float = value
        self.is_max_node: bool = is_max_node
        self.alpha: float = alpha
        self.beta: float = beta
        self.children: dict[Action, Self] = {}
        AgentProgram.leaf_nodes_alive += 1
        
    def __del__(self):
        if self.expanded:
            assert AgentProgram.parent_nodes_alive
            AgentProgram.parent_nodes_alive -= 1
        else:
            assert AgentProgram.leaf_nodes_alive
            AgentProgram.leaf_nodes_alive -= 1

@dataclass
class AgentProgram:
    """Class representing an agent program, which implements the agent function."""

    def __call__(self, percept: Percept) -> Action:
        self.__game = Game(percept.state)
        self.__player = percept.state.board.turn
        self.__root = AlphaBetaNode(state=percept.state,
                                    is_max_node=True,
                                    value=self.__eval(percept.state),
                                    alpha=0.0,
                                    beta=float('inf'))
        start_time = time()

        while time() - start_time < TIME_LIMIT:
            if self.__root.value == float('inf'):
                action = max(self.__root.children, key=lambda p: self.__root.children[p].value)
                return action

            if self.__root.value == 0:
                return None
            
            node = self.__next()
            self.__expand(node)
            self.__prune(node)
            
            if DEBUG:
                print("Parents alive: ", AgentProgram.parent_nodes_alive,
                      ", Leaves alive: ", AgentProgram.leaf_nodes_alive)
        
        action = max(self.__root.children, key=lambda p: self.__root.children[p].value)
        return action

    def __child_node(self, parent: AlphaBetaNode, action: Action) -> AlphaBetaNode:
        state = self.__game.result(parent.state, action)
        value = self.__eval(state, parent.state)
        is_max_node = not parent.is_max_node
        alpha = parent.alpha
        beta = parent.beta
        
        child = AlphaBetaNode(state=state,
                              parent=parent,
                              action=action,
                              value=value,
                              is_max_node=is_max_node,
                              alpha=alpha,
                              beta=beta)
        parent.children[action] = child

        return child

    def __eval(self, s: State, s_parent: State = None) -> float:
        if self.__game.terminal_test(s):
            return self.__game.utility(s, self.__player)
        
        def pieces_value(color: bool) -> float:
            pawns = len(s.board.pieces(chess.PAWN, color))
            knights = len(s.board.pieces(chess.KNIGHT, color))
            bishops = len(s.board.pieces(chess.BISHOP, color))
            rooks = len(s.board.pieces(chess.ROOK, color))
            queens = len(s.board.pieces(chess.QUEEN, color))
            value: float = pawns + knights*2.0 + bishops*3.0 + rooks*5.0 + queens*9.0
            
            return value
        
        w_pieces = pieces_value(chess.WHITE)
        b_pieces = pieces_value(chess.BLACK)

        move_count = s.board.legal_moves.count()
        parent_move_count = s_parent.board.legal_moves.count() if s_parent else move_count
        
        move_num = 0
        move_den = 0

        if s.board.turn == self.__player:
            move_num = move_count
            move_den = parent_move_count
        else:
            move_num = parent_move_count
            move_den = move_count
            
        pieces_num = 0
        pieces_den = 0
        
        if self.__player == chess.WHITE:
            pieces_num = w_pieces
            pieces_den = b_pieces
        else:
            pieces_num = b_pieces
            pieces_den = w_pieces
        
        move_ratio = float('inf') if move_den == 0 else move_num / move_den
        pieces_ratio = float('inf') if pieces_den == 0 else pieces_num / pieces_den

        eval_ = move_ratio * pieces_ratio
        return eval_

    def __expand(self, node: AlphaBetaNode):
        s = node.state
        is_max_node = node.is_max_node
        node.value = 0 if is_max_node else float('inf')

        for a in self.__game.actions(s):
            self.__child_node(node, a)

        node.expanded = True
        
        assert AgentProgram.leaf_nodes_alive
        AgentProgram.leaf_nodes_alive -= 1
        AgentProgram.parent_nodes_alive += 1

    def __next(self) -> AlphaBetaNode:
        node = self.__root

        while node.expanded:
            is_max_node = node.is_max_node
            actions = sorted(node.children, key=lambda p: node.children[p].value, reverse=is_max_node)
            a = len(actions) - 1
            rand = int(round(abs(uniform(-a, a))))
            action = actions[rand]
            node = node.children[action]

        return node

    def __prune(self, node: AlphaBetaNode):
        while node:
            if node.parent:
                node.alpha = max(node.alpha, node.parent.alpha)
                node.beta = min(node.beta, node.parent.beta)
            
            is_max_node = node.is_max_node
            node.value = 0 if is_max_node else float('inf')
            all_children_expanded = True

            for a, child in node.children.items():
                if not child.expanded:
                    all_children_expanded = False
                    break
                
            if is_max_node:
                action = max(node.children, key=lambda a: node.children[a].value)
                node.value = node.children[action].value
                node.alpha = max(node.alpha, node.value)
            else:
                action = min(node.children, key=lambda a: node.children[a].value)
                node.value = node.children[action].value
                node.beta = min(node.beta, node.value)
            
            if all_children_expanded:
                children: dict[Action, AlphaBetaNode] = {}
                
                for a, child in node.children.items():
                    if child.value == node.value:
                        children[a] = child
                
                node.children.clear()
                node.children = children

            node = node.parent

    __game: Game = None
    __player: bool = None
    __root: AlphaBetaNode = None

    leaf_nodes_alive: ClassVar[int] = 0
    parent_nodes_alive: ClassVar[int] = 0
