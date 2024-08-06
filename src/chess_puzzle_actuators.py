"""Module providing the ChessPuzzleActuators class."""

from dataclasses import dataclass

from actuators import Actuators
from chess_puzzle_action import ChessPuzzleAction
from chess_puzzle_environment import ChessPuzzleEnvironment

@dataclass
class ChessPuzzleActuators(Actuators):
    """Class representing chess puzzle actuators."""

    def __call__(self, action: ChessPuzzleAction, environment: ChessPuzzleEnvironment):
        if action.thinking:
            # Add code for displaying considered moves
            assert 0
        else:
            board = environment.game.board()
            board.push(action.move)
