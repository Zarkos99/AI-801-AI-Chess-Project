"""Module providing the Actuators class."""

from dataclasses import dataclass

import chess
from action import Action
from environment import Environment


@dataclass
class Actuators:
    """Class representing actuators, through which an agent can act upon its environment."""

    # Make FEN formatted moves with below (Nf3 as an example)
    # board.push(Nf3)
    # Undo moves with board.pop()
    # board.outcome() to determine outcome of new board state post-move

    def __call__(self, action: Action, environment: Environment):
        pass

    # TODO: Not certain if board is mutable in this context and therefore being passed by reference,
    # need to confirm once operational
    def move(self, board: chess.Board, from_space, to_space):
        """Conduct a move on the chess board and add it to the stack"""
        move = chess.Move(from_space, to_space)
        if board.is_legal(move):
            board.push(move)
        else:
            print("Illegal move: " + move)

    # TODO: Not certain if board is mutable in this context and therefore being passed by reference,
    # need to confirm once operational
    def undo_prev_move(self, board: chess.Board):
        """Pop a previous move from the stack"""
        board.pop()
