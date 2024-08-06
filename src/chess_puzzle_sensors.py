"""Module providing the ChessPuzzleSensors class."""

from dataclasses import dataclass

from chess_puzzle_environment import ChessPuzzleEnvironment
from chess_puzzle_percept import ChessPuzzlePercept
from chess_puzzle_state import ChessPuzzleState
from sensors import Sensors

@dataclass
class ChessPuzzleSensors(Sensors):
    """Class representing chess puzzle sensors."""

    def __call__(self, environment: ChessPuzzleEnvironment) -> ChessPuzzlePercept:
        state = ChessPuzzleState(environment.game.board())
        time_remaining = environment.time_remaining
        percept = ChessPuzzlePercept(state=state, time_remaining=time_remaining)

        return percept
